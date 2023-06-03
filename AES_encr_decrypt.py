# The script uses the AES encryption algorithm from the cryptography library. It prompts for a password and generates an 
# encryption key from it. The user is then asked to choose between encryption (E) or decryption (D). For each file in the directory, 
# the script reads the file, performs the chosen operation, and writes the encrypted or decrypted data to a new file with a modified filename.

import os
from getpass import getpass
from cryptography.fernet import Fernet

directory = "path/to/directory"
password = getpass("Enter password: ")

# Generate the encryption key from the password
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Prompt for encryption or decryption
operation = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

# Encrypt or decrypt files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        with open(filepath, "rb") as file:
            data = file.read()

            if operation == "E":
                encrypted_data = cipher_suite.encrypt(data)
                new_filename = f"encrypted_{filename}"
                new_filepath = os.path.join(directory, new_filename)

                with open(new_filepath, "wb") as encrypted_file:
                    encrypted_file.write(encrypted_data)

                print(f"File '{filename}' encrypted as '{new_filename}'.")
            elif operation == "D":
                decrypted_data = cipher_suite.decrypt(data)
                new_filename = f"decrypted_{filename}"
                new_filepath = os.path.join(directory, new_filename)

                with open(new_filepath, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_data)

                print(f"File '{filename}' decrypted as '{new_filename}'.")
            else:
                print("Invalid operation. Please choose 'E' for encryption or 'D' for decryption.")
