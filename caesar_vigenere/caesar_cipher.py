# Caesar Cipher Implementation
def caesar_cipher_encrypt(text, shift, alphabet):
    """Encrypt text using Caesar Cipher."""
    encrypted_text = ""
    for char in text.upper():
        if char in alphabet:
            new_position = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char  # Keep non-alphabetic characters
    return encrypted_text

def caesar_cipher_decrypt(text, shift, alphabet):
    """Decrypt text using Caesar Cipher."""
    decrypted_text = ""
    for char in text.upper():
        if char in alphabet:
            new_position = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char  # Keep non-alphabetic characters
    return decrypted_text
