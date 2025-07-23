
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i+1}. [{status}] {task['task']}")

def mark_complete(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["completed"] = True
        print(f"Task {task_number} marked as complete.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as complete: "))
            mark_complete(task_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
