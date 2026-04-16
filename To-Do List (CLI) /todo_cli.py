import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

# Add a task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append("[ ] " + task)
    print("Task added!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Deleted: {removed}")
    except:
        print("Invalid input!")

# Mark task as completed
def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[✔]")
        print("Task marked as completed!")
    except:
        print("Invalid input!")

# Main menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
