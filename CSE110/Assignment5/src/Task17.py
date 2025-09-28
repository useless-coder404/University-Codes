user_input = input().split(",")
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])
print(f"My list: {user_input}")

largest = user_input[0]
smallest = user_input[0]

index1 = 0
index2 = 0

for i in range(len(user_input)):
    if (user_input[i] < smallest):
        smallest = user_input[i]
        index1 = i
    if (user_input[i] > largest):
        largest = user_input[i]
        index2 = i
print("Smallest number in the list is", smallest, end=" ")
print("which was found at index", index1)
print("Largest number in the list is", largest, end=" ")
print("which was found at index", index2)
