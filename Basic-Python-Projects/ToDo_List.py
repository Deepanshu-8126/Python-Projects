# Simple To-Do List App
tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task removed!")
        else:
            print("Invalid number!")
    elif choice == "4":
        print("Exiting... bye ")
        break
    else:
        print("Invalid choice, try again.")
