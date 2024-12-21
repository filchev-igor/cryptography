from rsa_module.rsa import RSA

def main():
    input_file = "checksums.txt"  # Specify the checksum file
    results = run_verification(input_file)

    if isinstance(results, str):  # If an error message is returned
        print(results)
        return

    # Print results
    print(f"{'File':<30} {'Status':<50}")
    print("-" * 80)
    for file, status in results:
        print(f"{file:<30} {status:<50}")


    p, q = 7, 13
    e = 5
    rsa = RSA(p, q, e)

    print("Public Key:", rsa.public_key)
    print("Private Key:", rsa.private_key)

    message = "HELLO"
    ciphertext = rsa.encrypt(message)
    print("Ciphertext:", ciphertext)

    decrypted_message = rsa.decrypt(ciphertext)
    print("Decrypted Message:", decrypted_message)

    signature = rsa.sign(message)
    print("Signature:", signature)

    is_valid = rsa.verify(message, signature)
    print("Signature Valid:", is_valid)

if __name__ == "__main__":
    main()
