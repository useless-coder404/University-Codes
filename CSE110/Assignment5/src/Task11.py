list_one = [1, 4, 3, 2, 5]
list_two = [8, 7, 6, 9]

flag = False

for i in list_one:
    if i in list_two:
        flag = True
        break

if flag:
    print("True")
else:
    print("False")
