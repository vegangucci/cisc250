# =============================================================================
# Student Name: Doniel O'Niel
# Lab Title: Lab 4 - Food Truck Order Queue
# Date: May 23, 2026
# =============================================================================

# Task 1.1: Create two lists
empty_order_queue = []
menu_items = ["Burger", "Hot Dog", "Fries", "Fried Chicken Wings", "Buffalo Chicken Wings", "Soda", "Bottled Water", "Local Drink"]
#task complete

# Task 1.2: Display a welcome message and create an infinite while loop
print("Welcome to the Food Truck!")


while True:
     #2.1
     print('Type "menu" to display the menu.\n'
           "Type 'done' to complete your order.\n"
           "Please enter items one at a time.\n"
           )
     userinput = input("Please enter the food items you want to order:")

     #2.2
     if userinput == "done":
          break

     #2.3
     elif userinput == "":
          continue

     #2.4
     if userinput not in menu_items:
     
          print("Sorry, that item is not on the menu. Please try again.")
          continue

     #2.5
     #else: 
          #quantity_input = int()




          #task 3 
          #3.1
          print(f"\nOriginal Order Queue:{order_queue}")
          print("\n--- Processing Orders as follows..")

          #3.2
          while order_queue:
               item = order_queue.pop(0)
               print(f"Fullfillinf:{item}({len(order_queue)}items left in the queue)")


 #3.3
               print("All orders entries were fullfilled successfully")
               

                
               








          



     





