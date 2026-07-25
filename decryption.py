from cryptography.fernet import Fernet, InvalidToken
from authentication import generate_key
import os


def decrypt_file(file_path, password):
    """
    Decrypts the selected encrypted file using the user's password.
    """

    # Generate key from password
    key = generate_key(password)

    cipher = Fernet(key)

    # Read encrypted file
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    try:
        # Decrypt data
        decrypted_data = cipher.decrypt(encrypted_data)

    except InvalidToken:
        raise Exception("Incorrect Password! Access Denied.")

    # Create output folder
    output_folder = "decrypted_files"
    os.makedirs(output_folder, exist_ok=True)

    # Remove .encrypted extension
    file_name = os.path.basename(file_path)

    if file_name.endswith(".encrypted"):
        file_name = file_name[:-10]

    output_path = os.path.join(output_folder, file_name)

    # Save decrypted file
    with open(output_path, "wb") as file:
        file.write(decrypted_data)

    return output_path