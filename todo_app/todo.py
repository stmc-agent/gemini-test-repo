# A simple command-line to-do list application

def print_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!")

def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i+1}. [{status}] {task['task']}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
