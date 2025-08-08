import json
import os

TODO_FILE = "todos.json"

def get_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

def add_task(task):
    todos = get_todos()
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print(f"Added task: {task}")

def list_tasks():
    todos = get_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos):
        status = "✓" if todo["completed"] else " "
        print(f"{i + 1}. [{status}] {todo['task']}")

def complete_task(task_number):
    todos = get_todos()
    if 0 < task_number <= len(todos):
        todos[task_number - 1]["completed"] = True
        save_todos(todos)
        print(f"Completed task: {todos[task_number - 1]['task']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do App")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to complete: "))
                complete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
