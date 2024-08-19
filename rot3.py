def rot13(s):
    result = []
    for v in s: 
        c = ord(v)

        if 'a' <= v <= 'z':
            c = ord('a') + (c - ord('a') + 13) % 26
        elif 'A' <= v <= 'Z':
            c = ord('A') + (c - ord('A') + 13) % 26
        
        result.append(chr(c))
    return ''.join(result)

s = input("rot13: ")

res = rot13(s)

print(res)