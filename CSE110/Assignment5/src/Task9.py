string = input()
string = string + " "
s = ""
a_list = []
for i in string:
    if (i != " "):
        s += i
    else:
        a_list.append(int(s))
        s = ""
print("Original list:", a_list)
new_list = []
for i in range(len(a_list)):
    if (a_list[i] % 2 == 0):
        continue
    else:
        new_list.append(a_list[i])
print("Modified list:", new_list)
