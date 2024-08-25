import base64

# Given hex string that needs to be decoded into bytes
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert the hex string to bytes
# The bytes.fromhex() method is used to decode the hex string to a byte sequence
byte_string = bytes.fromhex(hex_string)

# Step 2: Encode the byte sequence to Base64
# The base64.b64encode() function is used to encode the byte sequence into a Base64 encoded string
base64_encoded = base64.b64encode(byte_string)

# Step 3: Convert the Base64 bytes to a string for readability (optional)
base64_string = base64_encoded.decode()

# Print the Base64 encoded string (flag)
print(base64_string)
