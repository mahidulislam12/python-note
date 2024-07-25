menu = {
    "pizza": 40,
    "pasta": 50,
    "coffee": 90,
    "salad": 20,
    "burger": 50,
}

# GREET
print("Welcome to Day Night Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}tk")

order_total = 0

# First item
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Order item '{item_1}' is not available yet!")

# Asking for another item
another_item = input("Do you want to add another item? (yes/no): ")
if another_item == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Order item '{item_2}' is not available yet!")
else:
    print("No additional items were added.")

# Print the total amount
print(f"Your total order amount is {order_total}tk.")
