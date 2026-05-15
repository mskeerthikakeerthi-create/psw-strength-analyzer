import re
import random
import string

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*()_+=]", password):
        score += 1

    if score <= 2:
        return "Weak Password"

    elif score == 3 or score == 4:
        return "Medium Password"

    else:
        return "Strong Password"


def suggest_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ''.join(random.choice(characters) for i in range(12))

    return password


password = input("Enter your password: ")

result = check_password_strength(password)

print("\nPassword Strength:", result)

if result == "Weak Password":
    print("Suggested Strong Password:", suggest_password())