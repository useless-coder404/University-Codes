string = input().split(",")

new_list = []
for x in string:
    clean_item = x.strip()
    number = int(clean_item)
    new_list.append(number)

string = new_list

print(f"Given numbers in list: {string}")

new_list = []
for i in string:
    if i not in new_list:
        new_list.append(i)

print(f"List without any duplicate values: {new_list}")
