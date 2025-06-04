import os

def list_directory(path):
    try:
        items = os.listdir(path)
        print(f"\n Contents of '{path}'\n")
        for idx, item in enumerate(items):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"{idx + 1}. [DIR] {item}")
            else:
                size = os.path.getsize(full_path)
                print(f"{idx + 1}. [FILE] {item} ({size} bytes)")
        return items
    except exception as e:
        print(f"Error accessing directory: {e}")
        return []
    
def cli_explorer():
    current_path = os.getcwd()

    while True:
        items = list_directory(current_path)

        print("\nOptions:")
        print("• Enter number to open folder")
        print("• '..' to go back")
        print("• 'exit' to quit")

        choice = input("Choose an option: ").strip()

        if choice == "exit":
            print("Exiting file explorer.")
            break
        elif choice == "..":
            current_path = os.path.dirname(current_path)
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                selected = os.path.join(current_path, items[idx])
                if os.path.isdir(selected):
                    current_path = selected
                else:
                    print(f"Selected item is a file: {items[idx]}")
            else:
                print("Invalid selection. Please try again.")
        else:
            print("Invalid input. Please enter a number, '..', or 'exit'.")

if __name__ == "__main__":
    print("Welcome to the CLI File Explorer!")
    cli_explorer()