
def encypt_func(txt, s):
    result = ""

    for i in range(len(txt)):
        char = txt[i]

        if(char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 65)
        else:
            result += chr((ord(char) + s - 96) % 26 + 97)
    return result

txt = "CAESAR CIPHER EXAMPLE PHRASE"
s = 4

print(txt)
print(str(s))
print(encypt_func(txt, s))