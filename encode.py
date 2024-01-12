def encrypt(text: str, key: int):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


key = 13
encrypted_code = encrypt("qrs", key)
print(encrypted_code)


# Path: decode.py
def decode(key: int):
    f = open("encrypted.txt", "r")
    text = encrypt(f.read(), -key)
    f.close()

    f = open("main.py", "w")
    f.write(text)
    f.close()


decode(-13)
