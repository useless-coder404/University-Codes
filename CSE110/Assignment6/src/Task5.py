given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
user_input = int(input())
count = 0
for item in given_tuple:
    if (user_input == item):
        count += 1
print(f"{user_input} appears {count} times in the tuple")
