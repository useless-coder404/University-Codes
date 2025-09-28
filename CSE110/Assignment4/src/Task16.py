string = input()
letter = input()
if letter in string:
    new_string = string.replace(letter, "")
    print(new_string)
elif (letter not in string) and (len(string) > 3):
    print(string[1:-1])
else:
    print(string)
