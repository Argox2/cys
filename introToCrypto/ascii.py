# Given integer array
integer_array = [99, 114, 121, 112, 116, 111, 123,
                 65, 83, 67, 73, 73, 95, 112, 114,
                 49, 110, 116, 52, 98, 108, 51, 125]
# Convert the integers to their corresponding ASCII characters
flag = ''.join(chr(i) for i in integer_array)

# Print the result
print(flag)
