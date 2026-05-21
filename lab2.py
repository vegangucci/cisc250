#Doniel O'Niel 

#question 1

#A
messy_menu = "    PizZA, burGER, SaLAd "
print(messy_menu.strip()) #the strip() method removes any leading and trailing whitespace from the string, so it will remove the extra spaces before and after the menu items.


#B
print(messy_menu.lower()) #the lower() method converts all characters in the string to lowercase, so it will change "PizZA" to "pizza", "burGER" to "burger", and "SaLAd" to "salad".

#C
clean_menu = f"{messy_menu.strip().lower()}"
print(f"Today's menu is: {clean_menu}") #the f-string allows us to format the string by including the cleaned menu within the output message. The strip() and lower() methods are applied to the messy_menu variable to clean it up before including it in the final output.

#question 2

#A
even_numbers = list(range(2, 51, 2))
print(even_numbers)

#B The list of numbers are provided in the word document
#C
print(len(even_numbers))  # prints the total number of items in the list

#D
print(sum(even_numbers))  # calculates the sum of all the number inside the list

#E
MULTIPLIER = 3
product = MULTIPLIER * (max(even_numbers) + min(even_numbers))
print(product)  # product of the multiplier with the sum of max and min values in thelist


#Question 3
#A
guest_list = ["Alice", "Bob", "Charlie", "Eve"] # a simple list of quest names
print(guest_list)

#B
guest_list.append("linus") #adding linus to the end of the list by append()
print(guest_list)

#C 
guest_list.insert(0, "guido") # adding guido to the beginning of the list
print(guest_list)

#D
guest_list.sort()  # sort the list alphabetically and permanently
print(guest_list)

#E
invitations = [f"You are invited, {name.capitalize()}!" for name in guest_list]
print(invitations)

#F
print(invitations[:3])  # print only the first three invitations

