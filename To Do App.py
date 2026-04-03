def task():
    tasks = []
    print("-----------Welcome to the Task Management App!----------")
    
    total_tasks = int(input("How many tasks do you want to add?: "))
    for i in range(total_tasks):
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append(task_name)
    print("All tasks added successfully!")
    print(f"Here are your tasks:\n{tasks}")
    
    while True:
        operation = int(input("Enter 1 to add a task\n2 to update\n3 to remove a task\n4 to view tasks\n5Exit/Stop\n->"))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print("Task added successfully!")
        elif operation == 2:
            update = input("Enter the task you want to update: ")
            if update in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Task updated successfully to: {up}")
        elif operation == 3:
            remove = input("Enter the task you want to remove: ")
            if remove in tasks:
                tasks.remove(remove)      #or ind = tasks.index[remove] 
                                          #   del tasks[ind]
                print("Task removed successfully!")
            else:
                print("Task not found!")
        elif operation == 4:
            print(f"Here are your tasks:\n{tasks}")
        elif operation == 5:
            print("Exiting the Task Management App. Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")

task()