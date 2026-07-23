def calculate_cart_total(*item_prices):
    # *item_prices saari prices ko ek tuple mein jama kar leta hai
    total = sum(item_prices)
    return total

# Ek customer ne 3 cheezein leen, dusre ne 5 cheezein leen
customer_a = calculate_cart_total(120, 450, 80)
customer_b = calculate_cart_total(10, 50, 100, 250, 1200)

print(f"Customer A Total: Rs. {customer_a}")
print(f"Customer B Total: Rs. {customer_b}")