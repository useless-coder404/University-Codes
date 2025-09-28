given_list = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]

key_list = []

for i in range(len(given_list)):
    keys = given_list[i][1]
    if keys not in key_list:
        key_list.append(keys)

my_dict = {}
for i in range(len(key_list)):
    new_list = []
    for count in range(len(given_list)):
        if key_list[i] == given_list[count][1]:
            new_list.append(given_list[count])
            my_dict[key_list[i]] = new_list
print(my_dict)
