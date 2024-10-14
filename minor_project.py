import json
from datetime import datetime, timedelta

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    status = 'Pending'
    task = {
        'description': description,
        'due_date': due_date,
        'status': status
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks with optional filtering
def view_tasks(tasks, filter_type=None):
    print("\nYour Tasks:")
    filtered_tasks = tasks
    if filter_type == 'completed':
        filtered_tasks = [task for task in tasks if task['status'] == 'Completed']
    elif filter_type == 'pending':
        filtered_tasks = [task for task in tasks if task['status'] == 'Pending']
    elif filter_type == 'due_soon':
        filtered_tasks = [task for task in tasks if task['due_date'] and is_due_soon(task['due_date'])]

    if not filtered_tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(filtered_tasks, 1):
            print(f"{idx}. {task['description']} - Due: {task['due_date']} - Status: {task['status']}")

# Check if task is due soon (within 3 days)
def is_due_soon(due_date_str):
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    return (due_date - datetime.today()).days <= 3

# Mark a task as complete
def mark_task_complete(tasks):
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    tasks[task_num]['status'] = 'Completed'
    save_tasks(tasks)
    print("Task marked as complete!")

# Edit a task
def edit_task(tasks):
    task_num = int(input("Enter task number to edit: ")) - 1
    new_description = input("Enter new task description: ")
    new_due_date = input("Enter new due date (YYYY-MM-DD): ")
    tasks[task_num]['description'] = new_description
    tasks[task_num]['due_date'] = new_due_date
    save_tasks(tasks)
    print("Task edited successfully!")

# Delete a task
def delete_task(tasks):
    task_num = int(input("Enter task number to delete: ")) - 1
    tasks.pop(task_num)
    save_tasks(tasks)
    print("Task deleted successfully!")

# Main menu
def menu():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View Pending Tasks")
        print("5. View Tasks Due Soon")
        print("6. Mark Task as Completed")
        print("7. Edit Task")
        print("8. Delete Task")
        print("9. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks, 'completed')
        elif choice == '4':
            view_tasks(tasks, 'pending')
        elif choice == '5':
            view_tasks(tasks, 'due_soon')
        elif choice == '6':
            mark_task_complete(tasks)
        elif choice == '7':
            edit_task(tasks)
        elif choice == '8':
            delete_task(tasks)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
