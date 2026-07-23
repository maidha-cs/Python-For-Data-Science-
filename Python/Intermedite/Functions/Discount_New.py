def get_discount_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

# Example: 5000 ka suit hai aur 20% off chal raha hai
shopping_bill = get_discount_price(5000, 20)
print(f"Bhai, 5000 wala item aapko Rs. {shopping_bill} ka milega.")