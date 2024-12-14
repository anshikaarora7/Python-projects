def display_todos(todos):
    if not todos:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")

def add_todo(todos):
    task = input("\nEnter a new task: ").strip()
    if task:
        todos.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")

def remove_todo(todos):
    display_todos(todos)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(todos):
            removed_task = todos.pop(task_num - 1)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    todos = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            display_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            remove_todo(todos)
        elif choice == "4":
            print("\nExiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
