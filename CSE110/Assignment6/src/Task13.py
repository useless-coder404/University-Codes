list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new_dict = {}

for item in list_1:
    key, value = item
    if key in new_dict:
        new_dict[key].append(value)
    else:
        new_dict[key] = [value]

print(new_dict)
