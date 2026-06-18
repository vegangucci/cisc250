# =============================================================================
# Student Name: Doniel O'Niel
# Lab Title: Lab 5
# Date: May 28, 2026
# =============================================================================

#1.1 Create a class called product
class Product:
    '''A class representing a product with a name and price.'''

    #1.2 Create an initializer method with three parameters. Stock has a default value of 0.
    def __init__(self, name, price, stock=0):
        '''Initializes a Product instance with a name, price, and stock quantity.'''
        self.name = name
        self.price = price
        self.stock = stock

    #1.3 Create a method called display_details()
    def display_details(self):
        '''Displays the details of the product in a user friendly format.'''
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")
        print("-" * 20)

    #1.4 Create a method called update_stock()
    def update_stock(self, amount):
        '''Updates the stock quantity by safely increasing or decreasing the value.'''
        if self.stock + amount >= 0:
            self.stock += amount
            print(f"Stock updated by {amount}.")
        else:
            print("ERROR: Stock cannot go below zero. No changes made.")


#Task 2: Define the Child/Derived class using Inheritance
#2.1 Create a child class that inherits from Product called DigitalProduct
class DigitalProduct(Product):
    '''A class representing a digital product, inheriting from Product.'''

    #2.2 Create the constructor/initializer method with name, price, and download_link.
    def __init__(self, name, price, download_link):
        '''Initializes a DigitalProduct instance with a name, price, and download link.'''
        super().__init__(name, price, 9999)
        self.download_link = download_link

    #2.3 Override the display_details method to show download link, not stock.
    def display_details(self):
        '''Displays the details of the digital product, excluding stock.'''
        print(f"Digital Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Download Link: {self.download_link}")
        print("-" * 20)


#Task 3: Instantiate and test your objects
#3.1 Create two objects: 1 Product and 1 DigitalProduct
product1 = Product("Laptop", 999.99, 10)
digital_product1 = DigitalProduct("E-book", 49.99, "www.downloadlink.com/ebook")

#3.2 Display initial details before any stock updates
print("Initial Product Details:")
product1.display_details()
print("Initial Digital Product Details:")
digital_product1.display_details()

# Positive update — increments stock above current value
print("Updating stock by +5")
product1.update_stock(5)
product1.display_details()

# Negative update — decrements stock but stays above zero
print("Updating stock by -8")
product1.update_stock(-8)
product1.display_details()

# Negative update — would bring stock below zero, should be blocked
print("Updating stock by -20")
product1.update_stock(-20)
product1.display_details()

#3.3 Display final digital product details
print("Digital Product Details:")
digital_product1.display_details()

 






 

