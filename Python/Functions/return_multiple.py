# Returning Multiple Values

def calculate(a, b):

    return a + b, a - b

sum_result, difference = calculate(10, 5)

print("Sum:", sum_result)
print("Difference:", difference)