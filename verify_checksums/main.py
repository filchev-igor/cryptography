from verify_checksums.checksums import main

def run():
    input_file = "checksums.txt"  # Relative path to checksums.txt
    results = main(input_file)

    if isinstance(results, str):  # If an error message is returned
        print(results)
        return

    # Print results
    print(f"{'File':<30} {'Status':<50}")
    print("-" * 80)
    for file, status in results:
        print(f"{file:<30} {status:<50}")

if __name__ == "__main__":
    run()
