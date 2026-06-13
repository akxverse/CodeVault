# Break and Continue

# break — stop loop when condition is met
print("Break Example:")

for i in range(1, 11):

    if i == 6:
        print("Stopping at 6!")
        break

    print(i)


# continue — skip even numbers
print("\nOdd Numbers Only (using continue):")

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)


# search in a list
names = ["Alice", "Bob", "Akanksha", "David"]

search = "Akanksha"

for name in names:

    if name == search:
        print(f"\nFound: {name}")
        break

else:
    print("Not found")