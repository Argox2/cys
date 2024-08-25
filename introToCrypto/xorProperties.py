# Import the binascii module to handle hexadecimal conversion
import binascii

# Given hex strings for KEY1, KEY2 ^ KEY1, and FLAG ^ KEY1 ^ KEY3 ^ KEY2
hex_key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
hex_key2_xor_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
hex_key2_xor_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
hex_flag_xor_key1_xor_key3_xor_key2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert the hex strings to bytes
key1 = binascii.unhexlify(hex_key1)
key2_xor_key1 = binascii.unhexlify(hex_key2_xor_key1)
key2_xor_key3 = binascii.unhexlify(hex_key2_xor_key3)
flag_xor_key1_xor_key3_xor_key2 = binascii.unhexlify(
    hex_flag_xor_key1_xor_key3_xor_key2)

# Step 1: Obtain KEY2 by XORing key2_xor_key1 with key1
key2 = bytes(a ^ b for a, b in zip(key1, key2_xor_key1))

# Step 2: Obtain KEY3 by XORing key2_xor_key3 with key2
key3 = bytes(a ^ b for a, b in zip(key2, key2_xor_key3))

# Step 3: Obtain the FLAG by XORing flag_xor_key1_xor_key3_xor_key2 with key1, key2, and key3
flag = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(
    flag_xor_key1_xor_key3_xor_key2, key1, key2, key3))

# Convert the FLAG from bytes to a string
flag_string = flag.decode()

# Print the flag
print(f"FLAG: crypto{{{flag_string}}}")
