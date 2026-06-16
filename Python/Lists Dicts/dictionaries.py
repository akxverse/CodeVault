# Dictionaries in Python

# Create a dictionary

student = {
    "name": "Alice",
    "age": 20,
    "marks": 92
}

# Access values

print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not Available"))

# Modify dictionary

student["age"] = 21
student["city"] = "Mumbai"

# Display dictionary

print("\nStudent Details:")

for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists

print("\n'name' exists:", "name" in student)
print("'phone' exists:", "phone" in student)