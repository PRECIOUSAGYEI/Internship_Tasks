import string
import secrets

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase   
    if use_lower:
        characters += string.ascii_lowercase   
    if use_digits:
        characters += string.digits           
    if use_special:
        characters += string.punctuation       

    if not characters:
        return "Error: You must select at least one character type."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


print("🛡  Random Password Generator")

while True:
    length = int(input("Enter desired password length : "))
    if length > 0:
        break
    else:
        print("Invalid input! Length must be a positive number.")

print("\nInclude the following character types?")
use_upper = input("Uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
use_lower = input("Lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
use_digits = input("Numbers (0-9)? (y/n): ").strip().lower() == 'y'
use_special = input("Special characters (!@#...)? (y/n): ").strip().lower() == 'y'

print("\nGenerating your secure password...\n")
result = generate_password(length, use_upper, use_lower, use_digits, use_special)
print("🔐 Your password is: ",result)
