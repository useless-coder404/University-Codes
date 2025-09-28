string = input()
for idx in range(len(string)):
    if string[idx] == "z":
        print("a", end="")
    else:
        print(chr(ord(string[idx])+1), end="")
