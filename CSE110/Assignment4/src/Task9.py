given_input = input()
length = len(given_input)
new_string = given_input[0]
for char in range(1, length):
    if given_input[char-1] != given_input[char]:
        new_string += given_input[char]
print(new_string)
