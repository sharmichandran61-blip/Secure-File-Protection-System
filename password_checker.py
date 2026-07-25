import re

# ==========================================
# Secure File Protection System
# Password Strength Checker
# ==========================================

def check_password_strength(password):
    """
    Returns:
    (Strength, Colour)
    """

    score = 0

    # Minimum Length
    if len(password) >= 8:
        score += 1

    # Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1

    # Number
    if re.search(r"[0-9]", password):
        score += 1

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Password Strength
    if score <= 2:
        return "Weak", "red"

    elif score == 3 or score == 4:
        return "Medium", "orange"

    else:
        return "Strong", "green"


# Test the file independently
if __name__ == "__main__":

    while True:

        password = input("Enter Password : ")

        strength, colour = check_password_strength(password)

        print(f"\nStrength : {strength}")
        print(f"Colour   : {colour}\n")