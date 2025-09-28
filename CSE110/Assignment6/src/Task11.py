user = input()
user = user.lower()
new_dict = {}
for char in user:
    if "a" <= char <= "z":
        if char not in new_dict:
            new_dict[char] = 1
        else:
            new_dict[char] += 1

print(new_dict)
