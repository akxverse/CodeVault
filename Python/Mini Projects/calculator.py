print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    print("Result =", a / b)

else:
    print("Invalid Choice")