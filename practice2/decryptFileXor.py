import os
import sys


def bruteForceXorKey(encrypted_data):

    magicNumber = b'MZ'
    for header_size in range(256):
        for key in range(256):
            decryptedData = bytes(
                [byte ^ key for byte in encrypted_data[
                    header_size:header_size + 2
                ]]
            )
            print(decryptedData)
            if decryptedData == magicNumber:
                print(f"Key: {key:#04x}")
                return key
    return None


def decryptedFile(inputFilePath, outputFilePath):
    if not os.path.exists(inputFilePath):
        print("File not found.")
    else:
        print("File found...")
        print("Getting the key...")
        with open(inputFilePath, 'rb') as f:
            encrypted_data = f.read()

        key = bruteForceXorKey(encrypted_data)

        if key is not None:
            decryptedData = bytes([byte ^ key for byte in encrypted_data])

            with open(outputFilePath, "wb") as fOut:
                fOut.write(decryptedData)
            print(f"File saved as: {outputFilePath}")
        else:
            print("Not valid key.")


inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

decryptedFile(inputFilePath, outputFilePath)
