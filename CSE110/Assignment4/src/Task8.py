string = input()
new_string = ""
for char in range(len(string)):
    if char % 2 != 0:
        new_string += chr(ord(string[char]) - 32)
print(new_string)
