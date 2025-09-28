def remove_odd(a_list):
    new_list = []
    for i in a_list:
        if i % 2 == 0:
            if i not in new_list:
                new_list.append(i)
            else:
                new_list.append(i)
    return new_list


a_list = input("Enter a listof numbers: ").split(",")

for i in range(len(a_list)):
    a_list[i] = int(a_list[i])

print(remove_odd(a_list))
