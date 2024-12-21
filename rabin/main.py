from rabin import Rabin

def main():
    # Use prime numbers satisfying p ≡ 3 (mod 4)
    p = 7   # Prime number
    q = 11  # Prime number
    rabin = Rabin(p, q)

    # Display keys
    print(f"Public Key (n): {rabin.n}")
    print(f"Private Key (p, q): ({p}, {q})")

    # Message to encrypt
    message = "HI"
    print(f"\nOriginal Message: {message}")

    try:
        # Encrypt message
        ciphertexts = rabin.encrypt(message)
        print(f"Ciphertexts: {ciphertexts}")

        # Decrypt message
        decrypted_messages = rabin.decrypt(ciphertexts)
        print(f"\nDecrypted Messages:")
        for msg in decrypted_messages:
            print(f"- {msg}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
