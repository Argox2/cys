import numpy as np

C1_Array = np.array(list("00000101000000000001111000000000"), dtype=int)
C2_Array = np.array(list("00011000000011100001100000001110"), dtype=int)
M1_Array = np.array(list("01101101011011110111001001100001"), dtype=int)

M2_Array = np.bitwise_xor(C1_Array, np.bitwise_xor(C2_Array, M1_Array))

M2 = ''.join(M2_Array.astype(str))

print("M2: ", M2)

K0_Array = np.bitwise_xor(C1_Array, M1_Array)

print("K0: ", K0_Array)

C2_Decryp = ''.join(np.bitwise_xor(K0_Array, C2_Array).astype(str))

binChunks = [C2_Decryp[i:i+8] for i in range(0, len(C2_Decryp), 8)]

C2_Text = ''.join([chr(int(chunk, 2)) for chunk in binChunks])

print("C2 Decrypted: ", C2_Text)
