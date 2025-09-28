user_input = input()
str1, str2 = user_input.split(', ')
mixed_string = ''

for i in range(min(len(str1), len(str2))):
    mixed_string += str1[i] + str2[i]

mixed_string += str1[len(str2):] + str2[len(str1):]

print(mixed_string)
