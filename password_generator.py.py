import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Prompt user for password length
    length = int(input("Enter the length of the password: "))
    # Generate password
    password = generate_password(length)
    # Display generated password
    print("Generated Password:", password)
