# Taking Input from User

name = input("Enter your name: ")
age = int(input("Enter your age: "))      # convert string to int
gpa = float(input("Enter your GPA: "))    # convert string to float

print("Hello,", name)
print("You are", age, "years old")
print("Your GPA is", gpa)

# f-string — modern clean way to print
print(f"Hi {name}! Age: {age}, GPA: {gpa}")