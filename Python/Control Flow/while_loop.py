# While Loop in Python

# Basic while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1      # same as count = count + 1


# While loop for input validation
while True:
    age = int(input("\nEnter age (must be positive): "))

    if age > 0:
        print(f"Valid age: {age}")
        break       # exit the loop

    else:
        print("Invalid! Try again.")


# While loop with counter
num = 1
total = 0

while num <= 10:
    total += num
    num += 1

print(f"Sum of 1 to 10 = {total}")