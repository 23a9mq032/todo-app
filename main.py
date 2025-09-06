print('Welcome to To-DO App')
def show_menu():
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
