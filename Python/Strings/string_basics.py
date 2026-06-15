# String Basics in Python

text = "Hello Python"

# Length

print(len(text))

# Access characters using index

print(text[0])
print(text[-1])

# Slicing

print(text[0:5])
print(text[6:])

# String methods

print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))
print(text.split(" "))

print(" hello ".strip())

# Check contents

print("Python" in text)
print(text.startswith("Hello"))