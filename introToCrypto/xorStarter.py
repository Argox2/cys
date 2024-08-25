# Given string and integer for XOR operation
input_string = "label"
xor_value = 13

# Initialize an empty list to store the XORed characters
xor_result = []

# Loop through each character in the string
for char in input_string:
    # Convert the character to its Unicode integer using ord()
    # XOR the Unicode integer with the given xor_value
    xor_char = ord(char) ^ xor_value
    # Convert the XORed integer back to a character using chr()
    xor_result.append(chr(xor_char))

# Join the XORed characters to form the new string
new_string = ''.join(xor_result)

# Format the flag as requested
flag = f"crypto{{{new_string}}}"

# Print the result
print(flag)
