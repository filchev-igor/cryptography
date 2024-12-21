# Vigenère Cipher Implementation
def vigenere_cipher_encrypt(plaintext, key, alphabet):
    """Encrypt text using Vigenère Cipher."""
    key = key.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    encrypted_text = ""
    key_index = 0

    for char in plaintext.upper():
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            new_position = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
            key_index += 1
        else:
            encrypted_text += char  # Keep non-alphabetic characters
    return encrypted_text

def vigenere_cipher_decrypt(ciphertext, key, alphabet):
    """Decrypt text using Vigenère Cipher."""
    key = key.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    decrypted_text = ""
    key_index = 0

    for char in ciphertext.upper():
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            new_position = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
            key_index += 1
        else:
            decrypted_text += char  # Keep non-alphabetic characters
    return decrypted_text
