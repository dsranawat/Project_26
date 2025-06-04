def is_valid_email(email):
    if '@' not in email or '.' not in email:
        return False
    if email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."):
        return False
    if ".." in email:
        return False
    
    at_index = email.index('@')
    dot_index = email.rindex(".")

    if at_index > dot_index:
        return False
    if len(email) - dot_index - 1 < 2:
        return False
    
    return True

def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

if __name__ == "__main__":
    main()