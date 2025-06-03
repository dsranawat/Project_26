def show_menu():
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    number = input("Enter number: ").strip()
    contacts.append((name, number))
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Saved Contacts:")
        for i, (name, number) in enumerate(contacts, start=1):
            print(f"{i}. {name} - {number}")

def search_contact(contacts):
    keyword = input("Enter name to search: ").strip().lower()
    found = False
    for name, number in contacts:
        if keyword in name.lower():
            print(f"Found: {name} - {number}")
            found = True
    if not found:
        print("No matching contacts found.")

def main():
    contacts = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact(contacts)   
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3': 
            search_contact(contacts)
        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()