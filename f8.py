#8.PASSWORD GENERATOR

import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    generated_password = generate_password(length)
    print(f"Your generated password is: {generated_password}")
