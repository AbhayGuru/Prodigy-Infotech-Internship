def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        print("[1] Encrypt.")
        print("[2] Decrypt.")
        print("[3] Exit.")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == "3":
            print("Exiting program... Goodbye!!!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()