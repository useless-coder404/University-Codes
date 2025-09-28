user_input = input().strip()
print(f"Original data: {user_input}")

user_input = user_input.strip("[]'\"")
print(f"After removing square brackets: {user_input}")

user_input = user_input.split(",")
print(f"Numbers in string format with extra white spaces: {user_input}")

new_list = []
for x in user_input:
    clean_item = x.strip()
    number = int(clean_item)
    new_list.append(number)

user_input = new_list
print(f"Final data (numbers in list format): {user_input}")
