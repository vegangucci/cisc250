# =============================================================================
# Student Name:
# Lab Title: Invoice Creator
# Date: 
# =============================================================================

# TASK 1: Nesting - Create a dictionary of dictionaries of the products being 
# purchased. Complete the nested dictionary below with the data in the lab 
# table.
product_list = {
    "el2234" : { 
        "name" : "Head Phones", 
        "category" : "Electronics", 
        "price" : 19.99, 
        "quantity" : 2 
        },
    "sh9989" : {
        "name" : "Running Shoes",
        "category" : "Footwear",
        "price" : 89.99,
        "quantity" : 1
    },
    "ap0098" : {
        "name" : "Smart Toaster",
        "category" : "Appliance",
        "price" : 130.00,
        "quantity" : 1
    },
    "cl3321" : {
        "name" : "Cotton Shirt",
        "category" : "Clothing",
        "price" : 10.00,
        "quantity" : 4
    },
    }
#Task 1 Completed.

# Task 2.1: Create a dictionary to hold the customer data

customer_data = {
    "Customer Name" : "Hannah Davis",
    "Loyalty Tier" : "Gold",
}
#task 2.1 Completed.

# Task 2.2: Print a processing order statement using an f string
print(f"Processing Order for: {customer_data['Customer Name']} [{customer_data['Loyalty Tier']} Tier Member]…")
#task 2.2 Completed.


# Task 3: Loop through dictionary with match-case discount calculations
total_after_discounts = 0

for product_id, product_info in product_list.items():
    subtotal = product_info["price"] * product_info["quantity"]
    
    match product_info["category"]:
        case "Appliance":
            discount_rate = 0.20
        case "Clothing":
            discount_rate = 0.10
        case _:
            discount_rate = 0.00
    
    sales_discount = subtotal * discount_rate
    final_product_price = subtotal - sales_discount
    total_after_discounts += final_product_price
    
    print(f"{product_info['name']}: Subtotal = ${subtotal:.2f}, Sales Discount = ${sales_discount:.2f}, Final Price = ${final_product_price:.2f}")

#Task 3 Completed.

# Task 4: Subtotals, membership discounts, and final invoice total
print(f"\nTotal after discounts: ${total_after_discounts:.2f}")

loyalty_tier = customer_data["Loyalty Tier"]

if loyalty_tier == "Platinum":
    membership_discount_rate = 0.16
elif loyalty_tier == "Gold":
    membership_discount_rate = 0.11
elif loyalty_tier == "Silver":
    membership_discount_rate = 0.05
else:
    membership_discount_rate = 0.00

membership_discount = total_after_discounts * membership_discount_rate
final_total = total_after_discounts - membership_discount

print(f"Membership Discount ({loyalty_tier} Tier): ${membership_discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
#Task 4 Completed.
