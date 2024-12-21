import os
import hashlib

def load_checksums(file_path):
    """Load checksums and file names from a text file."""
    checksums = {}
    try:
        # Ensure file_path is relative to the current script's directory
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(full_path, "r") as f:
            for line in f:
                parts = line.strip().split("  ")  # Format: "checksum  filename"
                if len(parts) == 2:
                    checksums[parts[1]] = parts[0]
    except FileNotFoundError:
        print(f"Error: Checksum file '{file_path}' not found.")
    return checksums

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    try:
        # File path should be relative to the `verify_checksums` folder
        full_path = os.path.join(os.path.dirname(__file__), "Eve v 0.4.AA", file_path)
        with open(full_path, "rb") as f:
            hasher = hashlib.md5()
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def verify_checksums(checksums):
    """Verify all files against the provided checksums."""
    results = []
    for file_name, expected_checksum in checksums.items():
        actual_checksum = calculate_md5(file_name)
        if actual_checksum is None:
            results.append((file_name, "File not found"))
        elif actual_checksum == expected_checksum:
            results.append((file_name, "Match"))
        else:
            results.append((file_name, f"Mismatch (Expected: {expected_checksum}, Got: {actual_checksum})"))
    return results

def main(input_file):
    """Run the verification process and return results."""
    checksums = load_checksums(input_file)
    if not checksums:
        return "No checksums to verify."
    return verify_checksums(checksums)
