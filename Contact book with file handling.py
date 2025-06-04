CONTACT_FILE = 'contacts.txt'

def add_contact(name, phone, email):
    with open(CONTACT_FILE, 'a') as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.")

def search_contact(name):
    found = False
    with open(CONTACT_FILE, "r") as file:
        for line in f:
            contact = line.strip().split(',')
            if contact[0].lower() == name.lower():
                print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
                found = True
    if not found:
        print("Contact not found.")

def delete_contact(name):
    contacts = []
    deleted = False
    with open(CONTACT_FILE, "r") as file:
        for line in f:
            if line.lower().startswith(name.lower() + ','):
                deleted = True
                continue
            contacts.append(line)
    with open(CONTACT_FILE, "w") as f:
        f.writelines(contacts)
    if deleted:
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        add_contact(name, phone, email)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)   
    elif choice == '4':
        print("Exiting the contact book.")
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()