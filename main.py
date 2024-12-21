from caesar_vigenere.caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt
from caesar_vigenere.vigenere_cipher import vigenere_cipher_encrypt, vigenere_cipher_decrypt

def main():
    # Variables
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = "Filchev Igor Att VGTU"
    secret_key = "I LIKE PARROTS"
    caesar_shift = 5

    print("Original Plaintext:", plaintext)

    # Caesar Cipher
    print("\n--- Caesar Cipher ---")
    caesar_encrypted = caesar_cipher_encrypt(plaintext, caesar_shift, alphabet)
    print("Encrypted Text:", caesar_encrypted)
    caesar_decrypted = caesar_cipher_decrypt(caesar_encrypted, caesar_shift, alphabet)
    print("Decrypted Text:", caesar_decrypted)

    # Vigenère Cipher
    print("\n--- Vigenère Cipher ---")
    vigenere_encrypted = vigenere_cipher_encrypt(plaintext, secret_key, alphabet)
    print("Encrypted Text:", vigenere_encrypted)
    vigenere_decrypted = vigenere_cipher_decrypt(vigenere_encrypted, secret_key, alphabet)
    print("Decrypted Text:", vigenere_decrypted)

if __name__ == "__main__":
    main()
