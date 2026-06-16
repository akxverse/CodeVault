# Lists in Python

fruits = ["apple", "banana", "mango", "orange"]

# Access elements

print(fruits[0])      # First element
print(fruits[-1])     # Last element
print(fruits[1:3])    # Slice

# Modify list

fruits.append("grape")        # Add at end
fruits.insert(1, "cherry")    # Add at index 1
fruits.remove("banana")       # Remove by value

popped = fruits.pop()         # Remove last item

print(fruits)

# Useful list operations

numbers = [5, 2, 8, 1, 9, 3]

print(sorted(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))