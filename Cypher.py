# Caesar cipher
text = input("Enter your message: ")
shift =""
while type(shift) != int:
    shift = input("enter shift value:")
    try:
        shift = int(shift)
    except:
        print("Invalid Shift value!!!")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + shift
    if code > ord('Z'):
        code = code - 26
    cipher += chr(code)
print(cipher)