from steganography.steganography import hide_data, reveal_data

def main():
    input_image = "files/input_image.png"       # Path to the input image
    output_image = "files/output_image.png"     # Path to save the modified image
    message_file = "files/secret_message.txt"   # Text file containing the secret message

    # Read the secret message from the text file
    with open(message_file, "r") as file:
        secret_message = file.read()

    # Hide the secret message
    print("Hiding the secret message...")
    hide_data(input_image, output_image, secret_message)
    print(f"Message hidden successfully in '{output_image}'.")

    # Reveal the secret message
    print("Revealing the hidden message...")
    revealed_message = kj,(output_image)
    print(f"Revealed Message: {revealed_message}")

if __name__ == "__main__":
    main()