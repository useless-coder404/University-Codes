my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None,
                 'd4': 'Blue', 'a5': None}
new_dict = {}
for key, val in my_dictionary.items():
    if val is not None:
        new_dict[key] = val

print(new_dict)
