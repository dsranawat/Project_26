import json
from datetime import datetime

Task_file = 'tasks.json'

def load_tasks():
    try:
        with open(Task_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(Task_file, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = input("Enter task title: ")
    deadline_str = input("Enter task deadline (YYYY-MM-DD HH:MM): ")

    try:
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        return
    
    task = {'title': title, 'deadline': deadline_str, 'completed': False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks scheduled.")
        return
    
    tasks.sort(key=lambda x: datetime.strptime(x['deadline'], '%Y-%m-%d %H:%M'))

    print("\n Daily Tasks List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔️" if task['completed'] else "🔄"
        print(f"{idx}. {task['title']} | Due: {task['deadline']} | Status: {status}")

def mark_task_complete():
    tasks = load_tasks()
    show_tasks()

    try:
        task_no = int(input("Enter task number to mark as complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['completed'] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nDaily Task Scheduler")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            print("Exiting the scheduler. Stay productive!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()