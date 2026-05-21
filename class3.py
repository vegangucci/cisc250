animals = ['dog', 'cat', 'cow', 'donkey', 'sheep']
if 'cow' in animals:
         print('mooo')
if 'pig' not in animals:
        print('no pigs found')


        age = 17
        if age >= 18:
            print("You are not eligible to vote!.")
        else:
         print("You are too young to vote!")
        print("Please register to vote as soon as you turn 19!.")




requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
      if requested_topping == 'green peppers':
         print("Sorry, we are out of green peppers right now.")
      else:
         print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")



status = 403
match status:
     case 400:
            print("Bad Request")
            