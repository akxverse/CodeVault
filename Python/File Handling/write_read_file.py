# Write and Read Files

# WRITE to a file
with open("notes.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("Python file handling is easy.\n")
    f.write("Line 3 here.\n")

print("File written!")

# READ entire file
with open("notes.txt", "r") as f:
    content = f.read()

print("\nFull content:")
print(content)

# READ line by line
with open("notes.txt", "r") as f:
    print("Line by line:")

    for line in f:
        print(line.strip())   # strip() removes '\n'

# APPEND to file
with open("notes.txt", "a") as f:
    f.write("This line was appended later.\n")

print("\nAppend done!")