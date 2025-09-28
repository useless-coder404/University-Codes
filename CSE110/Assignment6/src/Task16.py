a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

a_list = list(a_tuple)

user_input = input()

for i in range(len(a_list)):
    a_list[i][2] = user_input

tup = tuple(a_list)
print(tup)
