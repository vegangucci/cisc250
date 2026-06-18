# =============================================================================
# Student Name: Doniel O'Niel
# Lab Title: Lab 5 
# Date: May 28, 2026
# =============================================================================


# Task 3.1: Import save and load functions from lab5_3
from lab5_3 import store_task_list, load_task_list

# Task 3.2 (commented out): original empty list initialization
# todo_list = []

#1.2 Create a function called add_task. This function takes a string as an argument and appends it to the todo_list. It also prints a statement that the task was added, use an f string to display the actual task added.
def add_task(task):
    '''Adds a task to the todo list and prints a confirmation message.'''
    todo_list.append(task)
    print(f"Task added!: {task}")

#1.3 Create a function called show_task. This functions displays every task in the todo list and numbers them at 1. If the todo list is empty, it shows a message stating that 
def show_task():
    '''Displays all tasks in the todo list with numbering. If the list is empty, it shows a message indicating that there are no tasks.'''
    if todo_list == []:
        print("There are no tasks in the todo List.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

#1.4 Create a function called remove_task. This functiion takes in an integer that is based on the number assigned to the task from show_task. So, it is a 1-based index. So, you have to compensate for that to remove the correct task from the list. Please ensure to handling invalid numbers/text
def remove_task(task_number):
    '''Removes a task from the todo list based on a 1-based index. Handles invalid input gracefully.'''
    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number. Please enter a valid number.")
    else:
        removed = todo_list[task_number - 1]
        del todo_list[task_number - 1]
        print(f"Task removed: {removed}")

#Task 2: Setup and User Input 
#2.1 Create a function called run_todo_app()
def run_todo_app():
    '''Runs the todo list application, allowing users to add, show, and remove tasks.'''
    #2.2 Inside the function, display a welcome message for the Todo app
    print("Welcome to the Todo App!")
    #2.3 After the welcome message, create an infinite loop to handle the menu display and user selection.
    while True:
        #2.4 
        print("\n=== Menu ===")
        print("1. Show All Tasks")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        choice = input("What would you like to do? Please select a number > ")
        #2.5 
        if choice == "1":
            show_task()
        elif choice == "2":
            task = input("Enter a task you want to add > ")
            if task.strip() == "":
                print("Task description cannot be empty. Please enter a valid task number.")
            else:
                add_task(task)
        elif choice == "3":
            show_task()
            if todo_list:
                try:
                    task_number = int(input("Please enter the number of the task you wish to remove >"))
                    remove_task(task_number)
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
        elif choice == "4":
            print("Thank you for using the Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

#2.6 Call the run_todo_app() function to start the application
if __name__ == "__main__":
    # Task 3.3: Load the task list before running the app
    todo_list = load_task_list()

    run_todo_app()

    # Task 3.4: Save the task list after the app exits
    store_task_list(todo_list)
  
    

    


           



    

        

            
