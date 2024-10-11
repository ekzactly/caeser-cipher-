# Function to encrypt the message
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char
    return decrypted_message

# Main function to take user input and perform encryption or decryption
if __name__ == "__main__":
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        print(f"Encrypted Message: {encrypt(message, shift)}")
    elif choice == 'd':
        print(f"Decrypted Message: {decrypt(message, shift)}")
    else:
        print("Invalid choice.")
