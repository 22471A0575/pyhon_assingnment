def show_menu():
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark as Completed")
    print("4. View Tasks")
    print("5. Completed Tasks")
    print("6. Quit")
tasks=list()
completed_tasks=list()
while True:
    show_menu()
    choice=input("Enter your choice (1-6): ")
    if choice=='1':
        task=input("Enter the task: ")
        tasks.append(task)
    elif choice=='2':
        task_index=int(input("Enter the task index to remove: "))
        i=task_index-1
        del tasks[i]
    elif choice=='3':
        task_index=int(input("Enter the task index to mark as completed: "))
        i=task_index-1
        a=tasks.pop(i)
        completed_tasks.append(a)
    elif choice=='4':
        print("your Tasks:")
        if len(tasks)==0:
            print("no Tasks added")
        else:
            for i in range(len(tasks)):
                print("{}.{}".format(i+1,tasks[i]))
    elif choice=='5':
        print("your completed Tasks")
        if len(completed_tasks)==0:
            print("no completed tasks")
        else:
            for i in range(len(completed_tasks)):
                print("{}.{}".format(i+1,completed_tasks[i]))
    elif choice=='6':
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
