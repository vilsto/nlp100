#08. 暗号文
def cipher(ciph):
    ciphed =""
    for l_char in ciph:
        if l_char.islower():
            ciphed += chr(219 - ord(l_char))
        else:
            ciphed += l_char
    return ciphed

def main():
    str_008 = "This is a message"
    print(str_008)
    print(cipher(str_008))

if __name__ == "__main__":
    main()