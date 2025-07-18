import string
import secrets

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""

    # Build the character pool based on user choices
    if use_upper:
        characters += string.ascii_uppercase   # A-Z
    if use_lower:
        characters += string.ascii_lowercase   # a-z
    if use_digits:
        characters += string.digits            # 0-9
    if use_special:
        characters += string.punctuation       # !@#$%^&*...

    if not characters:
        return "Error: You must select at least one character type."

    # Use secrets module for strong randomness
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# ---------- MAIN PROGRAM ----------
print("🛡  Random Password Generator")

# 1. Ask user for password length
while True:
    length = int(input("Enter desired password length (e.g. 8, 12, 16): "))
    if length > 0:
        break
    else:
        print("Invalid input! Length must be a positive number.")

# 2. Ask user which character types to include
print("\nInclude the following character types?")
use_upper = input("Uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
use_lower = input("Lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
use_digits = input("Numbers (0-9)? (y/n): ").strip().lower() == 'y'
use_special = input("Special characters (!@#...)? (y/n): ").strip().lower() == 'y'

# 3. Generate and display the password
print("\nGenerating your secure password...\n")
result = generate_password(length, use_upper, use_lower, use_digits, use_special)
print("🔐 Your password is: ",result)
