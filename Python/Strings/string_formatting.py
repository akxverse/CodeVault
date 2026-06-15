# String Formatting in Python

product = "Laptop"
price = 59999.99
quantity = 2

# f-string (recommended)

print(f"Product: {product}")
print(f"Price: ₹{price:.2f}")
print(f"Quantity: {quantity}")

# Calculate total cost

total = price * quantity

print(f"Total Cost: ₹{total:.2f}")

# Using .format()

print("\nProduct: {}, Price: ₹{}".format(product, price))

# Table-like formatting

print("\nInventory")
print(f"{'Product':<15}{'Price':>10}")
print(f"{product:<15}{price:>10.2f}")