# Store Student Data in a File

name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("students.txt", "a") as file:
    file.write(f"{name} - {marks}\n")

print("Student record saved.")

print("\nStudent Records:")

with open("students.txt", "r") as file:
    print(file.read())
