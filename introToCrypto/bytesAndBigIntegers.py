from Crypto.Util.number import long_to_bytes

# Given large integer that needs to be converted back into a message
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the large integer back to bytes
# The long_to_bytes() function is used to convert the integer to its corresponding byte sequence
byte_message = long_to_bytes(large_integer)

# Decode the byte sequence to get the ASCII characters (message)
# The decode() method converts the bytes back into a string
message = byte_message.decode()

# Print the resulting message
print(message)
