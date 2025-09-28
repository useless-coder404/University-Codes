def remove_list(lst):
    new_list = []
    count = 0
    for i in lst:
        if new_list.count(i) < 2:
            new_list.append(i)
        else:
            count += 1
    print(f"Removed: {count}")
    return new_list


lst = input().split(",")

for i in range(len(lst)):
    lst[i] = int(lst[i])

print(remove_list(lst))
