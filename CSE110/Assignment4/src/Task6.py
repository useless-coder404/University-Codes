string = input()
for idx in range(len(string)):
    slicing = string[idx:idx+1:]
    ascii = ord(slicing)
    print(slicing, ":", ascii)
