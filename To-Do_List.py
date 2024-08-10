# For adding a task 
def add_task(task, filename="tasks.txt"):
    with open(filename, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added.")


# For viewing the added tasks
def view_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Your To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("Your To-Do List is empty.")
    except FileNotFoundError:
        print("No tasks found. Start by adding a new task.")


# For delete a task
def delete_task(task_number, filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()

        if 0 < task_number <= len(tasks):
            task = tasks.pop(task_number - 1).strip()
            with open(filename, "w") as file:
                file.writelines(tasks)
            print(f"Task '{task}' deleted.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found. Start by adding a new task.")


# Main function for implement the CLI logic
def main():
    while True:
        print("\nSimple To-Do List CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Thank you for using !")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
