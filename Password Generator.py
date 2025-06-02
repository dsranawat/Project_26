import random
import string

print("Basic Password Generator")

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4 characters."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = [ random.choice(lowercase),
                        random.choice(uppercase),
                        random.choice(digits),
                        random.choice(symbols) ]
    
    if length > 4:
        all_chars = lowercase + uppercase + digits + symbols
        password_chars += random.choices(all_chars, k=length - 4)
    
    random.shuffle(password_chars)
    return ''.join(password_chars)

while True:
    try:
        length_input = input("Enter desired password length (or 'q' to quit): ")

        if length_input.lower() == 'q':
            print("Exiting the password generator. Goodbye!")
            break

        length = int(length_input)
        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for password length or 'q' to quit.")
