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
while menu_items:
     print("Welcome to the Food Truck! Please place your order.")
#task complete


# Task 2: Setup user input
while True:
     print('Type "menu" to display the menu, "done" to complete your order, and enter items one at a time.')
     current_order = []
     while True:
          user_input = input("Please Enter an item (or 'menu'/'done'): ").strip()
          if not user_input:
               print("No input entered. Please enter a menu item, 'menu', or 'done'.")
               continue
          if user_input.lower() == "menu":
               print("Menu:")
               for m in menu_items:
                    print("-", m)
               continue
          if user_input.lower() == "done":
               if current_order:
                    print("Your order:", ", ".join(current_order))
                    empty_order_queue.append(current_order)
               else:
                    print("No items were added to your order.")
               break
          matched = None
          for m in menu_items:
               if m.lower() == user_input.lower():
                    matched = m
                    break
          if not matched:
               print(f"'{user_input}' is not on the menu. Type 'menu' to see available items.")
               continue
          while True:
               quantity_input = input(f"How many {matched} would you like? ").strip()
               if not quantity_input:
                    print("Quantity cannot be empty. Please enter a positive whole number.")
                    continue
               if not quantity_input.isdigit():
                    print("Invalid quantity. Please enter a whole number.")
                    continue
               quantity = int(quantity_input)
               if quantity <= 0:
                    print("Quantity must be at least 1.")
                    continue
               break
          current_order.extend([matched] * quantity)
          print(f"Added {quantity} x {matched} to your order.")

     more = input("Take another order? (y/n): ").strip().lower()
     if more not in ("y", "yes"):
          print("Closing orders. Goodbye!")
          break
#task complete

# Task 3: Process the order queue
print("Order queue to be processed:")
print(empty_order_queue)
while empty_order_queue:
     current_item = empty_order_queue.pop(0)
     remaining = len(empty_order_queue)
     print(f"Fulfilling: {current_item}... ({remaining} items remaining in queue)")
print("All order entries were fulfilled successfully.") 
#task complete