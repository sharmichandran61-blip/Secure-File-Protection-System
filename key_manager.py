from cryptography.fernet import Fernet
import os

# ==========================================
# Secure File Protection System
# Key Management Module
# ==========================================

# Folder to store encryption key
KEY_FOLDER = "keys"

# Key file name
KEY_FILE = os.path.join(KEY_FOLDER, "secret.key")


def generate_key():
    """
    Generates a new encryption key if it does not exist.
    """

    # Create keys folder if it doesn't exist
    os.makedirs(KEY_FOLDER, exist_ok=True)

    # Generate key only once
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)


def load_key():
    """
    Loads the existing encryption key.
    If the key is missing, it will be created automatically.
    """

    generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def delete_key():
    """
    Deletes the encryption key.
    (Optional utility function)
    """

    if os.path.exists(KEY_FILE):
        os.remove(KEY_FILE)


def key_exists():
    """
    Returns True if the encryption key exists.
    """

    return os.path.exists(KEY_FILE)


# Run only when this file is executed directly
if __name__ == "__main__":

    generate_key()

    if key_exists():
        print("Encryption Key Created Successfully!")
    else:
        print("Failed to Create Encryption Key.")