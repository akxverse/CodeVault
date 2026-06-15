# String Methods in Python

text = "python programming"

# Change case

print(text.upper())
print(text.lower())
print(text.title())

# Replace text

print(text.replace("python", "Python"))

# Count occurrences

print(text.count("m"))

# Find position

print(text.find("program"))

# Split into a list

words = text.split(" ")
print(words)

# Join list into a string

joined = "-".join(words)
print(joined)

# Check string content

print("hello".isalpha())
print("123".isdigit())
print("hello123".isalnum())