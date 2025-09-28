given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

a_list = list(given_tuple)

new_list = []

for i in range(len(a_list)-1, -1, -1):
    new_list.append(a_list[i])

tup = tuple(new_list)

print(tup)
