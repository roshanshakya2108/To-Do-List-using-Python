import os

# File to store tasks
TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "done": status == "done"})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "pending"
            file.write(f"{task['task']} | {status}\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")


def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def mark_done(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to mark as done: "))
            if 1 <= index <= len(tasks):
                tasks[index - 1]["done"] = True
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"Task '{removed_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List App ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
