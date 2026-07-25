from cryptography.fernet import Fernet
from authentication import generate_key
import os


def encrypt_file(file_path, password):
    """
    Encrypts the selected file using the user's password.
    """

    # Generate key from password
    key = generate_key(password)

    cipher = Fernet(key)

    # Read original file
    with open(file_path, "rb") as file:
        data = file.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(data)

    # Create output folder
    output_folder = "encrypted_files"
    os.makedirs(output_folder, exist_ok=True)

    # Create encrypted filename
    file_name = os.path.basename(file_path)
    output_path = os.path.join(
        output_folder,
        file_name + ".encrypted"
    )

    # Save encrypted file
    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    return output_path