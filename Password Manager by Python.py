import random
import string

def generate_password(length, complexity):
    # Define character sets
    if complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    # Generate password
    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    print("🔐 Welcome to the Password Generator Application 🔐")

    while True:
        # Get password length from user
        while True:
            try:
                length = int(input("Enter the desired password length (8-128): "))
                if 8 <= length <= 128:
                    break
                else:
                    print("Password length must be between 8 and 128.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get password complexity from user
        while True:
            complexity = input("Do you want a strong password? (yes/no): ").strip().lower()
            if complexity in ("yes", "no"):
                complexity = "strong" if complexity == "yes" else "simple"
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        # Generate and display password
        password = generate_password(length, complexity)
        print("\n🎉 Generated Password: ", password)

        # Option to copy password to clipboard
        try:
            import pyperclip
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")
        except ImportError:
            print("Install 'pyperclip' to enable clipboard functionality.")

        # Ask user if they want to generate another password
        while True:
            another = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
            if another == "yes":
                break
            elif another == "no":
                print("Goodbye! Stay secure. 🔒")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    password_generator()


