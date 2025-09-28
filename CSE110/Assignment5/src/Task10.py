string = input().split(",")
for i in range(len(string)):
    string[i] = int(string[i])
print("Input list:", string)

new_list = []
for i in string:
    if i not in new_list:
        new_list.append(i)
print("Modified list: ", new_list)
