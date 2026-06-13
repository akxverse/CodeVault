# For Loop in Python

# Loop using range(start, stop, step)
print("Numbers 1 to 5:")

for i in range(1, 6):
    print(i)

# Loop through a list
fruits = ["apple", "banana", "mango", "orange"]

print("\nFruits:")

for fruit in fruits:
    print("-", fruit)

# Loop through a string (character by character)
name = "Akanksha"

print("\nLetters:")

for letter in name:
    print(letter, end=" ")   # end=" " keeps output on same line

# Loop with index using enumerate()
print("\n\nWith Index:")

for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")