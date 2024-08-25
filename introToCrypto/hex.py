# Given hexadecimal string representing encoded bytes
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert the hexadecimal string into bytes
# The bytes.fromhex() method converts the hex string to its corresponding byte
# representation
byte_string = bytes.fromhex(hex_string)

# Decode the byte string to get the ASCII characters (flag)
# The decode() method converts the bytes back into a string
flag = byte_string.decode()

# Print the resulting flag
print(flag)
