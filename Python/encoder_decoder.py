text = input("Enter message: ")

encoded = ""

for ch in text:
    encoded = encoded + chr(ord(ch) + 1)

print("Encoded message =", encoded)

decoded = ""

for ch in encoded:
    decoded = decoded + chr(ord(ch) - 1)

print("Decoded message =", decoded)