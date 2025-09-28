string = input()
is_binary = True
for char in range(len(string)):
    if (string[char] != "0" and string[char] != "1"):
        is_binary = False
        break
if is_binary:
    print("Binary Number")
else:
    print("Not a Binary Number")
