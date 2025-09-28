given_list = [(11, 22), (33, 55), (55, 77), (11, 44)]

new_list = []

for i in range(0, len(given_list)):
    multiple = given_list[i][0] * given_list[i][1]
    new_list.append(multiple)

print(new_list)
