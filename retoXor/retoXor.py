import numpy as np


# Primero transformamos las strings a arrays.
C1_Array = np.array(list("00000101000000000001111000000000"), dtype=int)
C2_Array = np.array(list("00011000000011100001100000001110"), dtype=int)
M1_Array = np.array(list("01101101011011110111001001100001"), dtype=int)

# Realizamos la operacion XOR para encontrar M2,
# que es el mensaje desecriptado de C2
M2_Array = np.bitwise_xor(C1_Array, np.bitwise_xor(C2_Array, M1_Array))
M2 = ''.join(M2_Array.astype(str))
print("M2: ", M2)

# Para obtener el mensaje.
# Dividir la string en cadenas de 8 bits.
binChunks = [M2[i:i+8] for i in range(0, len(M2), 8)]

# Transformar los pedazos de 8 bits a su decimal,
# y luego eso a su codigo ASCII.
M2_Text = ''.join([chr(int(chunk, 2)) for chunk in binChunks])

# Por ultimo imprimimos el mensaje decifrado.
print("M2 message: ", M2_Text)
