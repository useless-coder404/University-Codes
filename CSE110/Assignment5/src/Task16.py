user_input = input().split(",")
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])
print(f"My list:{user_input}")

largest = user_input[0]
second_largest = float('-inf')
index = -1

for i in range(1, len(user_input)):
    if (user_input[i] > largest):
        second_largest = largest
        largest = user_input[i]
        index = i
    elif (user_input[i] > second_largest and user_input[i] < largest):
        second_largest = user_input[i]
        index = i

print("Second largest number in the list is", second_largest, end=" ")
print("which was found at index", index)
