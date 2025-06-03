def menu():
    print("Welcome to the To-Do List App!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter Task: ")
    task_list.append(task)
    print("Task added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks to show.")
    else:
        print("tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(task_list):
            removed = task_list.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List App.\nGoodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()