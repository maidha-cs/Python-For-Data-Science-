item_name = input("Write Dish Name: ")
price = float(input("Price of One Plate: "))
quantity = int(input("How much plates? "))
Item_Total = price * quantity
With_Tax= Item_Total * 0.10
Total_Bill = Item_Total + With_Tax
print(" ======Generate Slip========")
print(f"item_name: {item_name}")
print(f"quantity: {quantity}")
print(f"Item_Total: {Item_Total}")
print(f"With_Tax: {With_Tax}")
print(f" Total_Bill: { Total_Bill}")

