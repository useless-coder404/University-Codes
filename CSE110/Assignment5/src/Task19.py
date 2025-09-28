list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
list_three = list_one + list_two

new_list = []

for i in list_three:
    if i not in new_list:
        new_list.append(i)
print(f"Output for the above two lists: {new_list}")
