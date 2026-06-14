# Functions in Python

# Define a function using 'def'
def greet(name):
    print(f"Hello, {name}! Welcome.")

# Call the function
greet("Akanksha")
greet("Alia")

# Function that returns a value
def add(a, b):
    return a + b

result = add(10, 5)

print(f"10 + 5 = {result}")


# Function with default parameter
def greet_formal(name, title="Ms."):
    print(f"Good morning, {title} {name}")

greet_formal("Singh")           # Uses default title