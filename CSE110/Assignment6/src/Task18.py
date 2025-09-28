dict_1 = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}

lower, upper = input().split(",")

new_dict = {}
for key, value in dict_1.items():
    if int(lower) <= value < int(upper):
        new_dict[key] = value
print(new_dict)
