# Tuples and Sets in Python

# Tuple

coordinates = (10.5, 20.3)

print("Coordinates:", coordinates)
print("First Value:", coordinates[0])

# Tuple unpacking

x, y = coordinates

print("x =", x)
print("y =", y)

# Set

numbers = {1, 2, 3, 2, 1, 4}

print("\nSet:", numbers)

# Add element

numbers.add(5)

print("After Adding 5:", numbers)

# Set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nUnion:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)