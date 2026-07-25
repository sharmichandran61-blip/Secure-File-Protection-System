import os
import base64
import hashlib

# ==========================================
# Password Authentication Module
# ==========================================

AUTH_FOLDER = "auth"
SALT_FILE = os.path.join(AUTH_FOLDER, "salt.bin")


def generate_salt():
    """
    Create a random salt only once.
    """

    os.makedirs(AUTH_FOLDER, exist_ok=True)

    if not os.path.exists(SALT_FILE):

        salt = os.urandom(16)

        with open(SALT_FILE, "wb") as file:
            file.write(salt)


def load_salt():
    """
    Load the existing salt.
    """

    generate_salt()

    with open(SALT_FILE, "rb") as file:
        return file.read()


def generate_key(password):
    """
    Generate a Fernet-compatible key from the password.
    """

    salt = load_salt()

    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return base64.urlsafe_b64encode(key)


def verify_password(password):
    """
    Check whether the password can generate a valid key.
    """

    try:
        generate_key(password)
        return True
    except:
        return False