string = input()
index = 0
new_string = ""
for i in range(0, len(string)):
    if string[i].isalpha():
        if index % 2 == 0:
            large = string[i].upper()
            new_string += large
            index += 1
        else:
            small = string[i].lower()
            new_string += small
            index += 1
    else:
        new_string += string[i]
print(new_string)
