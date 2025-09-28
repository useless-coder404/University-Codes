list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
list_three = list_one + list_two

new_list = []
for i in list_three:
    if (i % 2 == 0):
        new_list.append(i)
print(new_list)
