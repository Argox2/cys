import requests

full_crypt_hex = '82a6f4f7a60f9798f167bf61232d7754824d8538ded42f7e4a53915327c07456'
full_crypt_bytes = bytes.fromhex(full_crypt_hex)

# Divide message in 16-byte blocks.
crypts = [full_crypt_bytes[i:i+16]
          for i in range(0, len(full_crypt_bytes), 16)]

C1 = crypts[0]
C2 = crypts[1]

I2 = [0] * 16
P2 = [0] * 16

url = "http://64.227.29.191/validador.cbc?ciphertext="


def check_padding(C1p, C2):
    ciphertext = (C1p + C2).hex()
    response = requests.get(url + ciphertext)
    print(url + ciphertext)
    return 'OK' in response.text


C1p = bytearray(C1)

for i in range(15, -1, -1):
    padding_value = 16 - i
    for guess in range(256):
        C1p = bytearray(C1p)
        C1p[i] = guess

        # Ajust next bytes.
        for j in range(i + 1, 16):
            C1p[j] = I2[j] ^ padding_value

        # Check padding.
        if check_padding(bytes(C1p), C2):
            I2[i] = guess ^ padding_value
            P2[i] = I2[i] ^ C1[i]
            print(f'Byte {i+1} recuperado: {P2[i]:02x}')
            break

plaintext = bytes(P2)
print('Texto plano recuperado: ', plaintext)
