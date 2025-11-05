# main.py

from task_manager_app.task import Task
from task_manager_app.file_handler import read_tasks, write_tasks
from task_manager_app.input_validator import get_valid_string, get_valid_priority

TASKS_FILE = "data/tasks.json"


# Display Menu
def main_menu():
    print("\n-----------------------------------")
    print("|     TASK MANAGER APPLICATION    |")
    print("-----------------------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------------------")


# Display Tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        print(f"\n{i + 1}. Name: {task.name}")
        print(f"   Desc: {task.description}")
        print(f"   Priority: {task.priority}")


# Run Application
def run_app():
    tasks = read_tasks(TASKS_FILE)  # Load tasks at start

    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add Task
            print("\n--- Add Task ---")
            name = get_valid_string("Enter task name: ")
            description = get_valid_string("Enter task description: ")
            priority = get_valid_priority("Enter task priority (Low/Medium/High): ")

            new_task = Task(name, description, priority)
            tasks.append(new_task)
            write_tasks(TASKS_FILE, tasks)
            print("✅ Task added successfully!")

        elif choice == '2':
            # View Tasks
            print("\n--- View Tasks ---")
            display_tasks(tasks)

        elif choice == '3':
            # Update Task
            print("\n--- Update Task ---")
            display_tasks(tasks)
            try:
                task_index = int(input("Enter task number to update: ")) - 1
                if 0 <= task_index < len(tasks):
                    print(f"Selected task: {tasks[task_index].name}")
                    tasks[task_index].name = get_valid_string("Enter new name: ")
                    tasks[task_index].description = get_valid_string("Enter new description: ")
                    tasks[task_index].priority = get_valid_priority("Enter new priority (Low/Medium/High): ")
                    write_tasks(TASKS_FILE, tasks)
                    print("✅ Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            # Delete Task
            print("\n--- Delete Task ---")
            display_tasks(tasks)
            try:
                task_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    write_tasks(TASKS_FILE, tasks)
                    print(f"🗑️ Task '{removed_task.name}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run_app()