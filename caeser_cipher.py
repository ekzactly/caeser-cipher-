# caesar_cipher.py

# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if it's an uppercase or lowercase letter
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and handle wrap-around using modulo
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text += encrypted_char
        else:
            # If it's not a letter, leave it unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr(((ord(char) - ascii_offset - shift) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Main function to take user input and perform encryption/decryption
def main():
    # Get user input for message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")

# Run the main function
if __name__ == "__main__":
    main()
