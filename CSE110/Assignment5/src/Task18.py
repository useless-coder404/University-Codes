list_one = input().split(",")
for i in range(len(list_one)):
    list_one[i] = list_one[i].strip()

list_two = input().split(",")
for i in range(len(list_two)):
    list_two[i] = list_two[i].strip()

new_list = []
for i in list_two:
    if i in list_one and i not in new_list:
        new_list.append(i)

print(new_list)
