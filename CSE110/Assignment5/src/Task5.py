given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
new_list = []
print(f"Original List: {given_list}")
for i in range(len(given_list)):
    if (given_list[i] != ""):
        new_list.append(given_list[i])
print(f"Modified List: {new_list}")
