# Type Conversion in Python

# int to float and back
x = 10
print(float(x))      # 10.0

y = 3.99
print(int(y))        # 3

# string to number
age_str = "20"
age_num = int(age_str)

print(age_num + 5)   # 25

# number to string
score = 95
message = "Your score: " + str(score)

print(message)

# check before converting
text = "hello"

print(text.isdigit())      # False
print("123".isdigit())     # True