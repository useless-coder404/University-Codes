string = input().split(",")
for i in range(len(string)):
    string[i] = int(string[i])

large = string[0]
index = 0
for i in range(len(string)):
    if (string[i] > large):
        large = string[i]
        index = i
print("My list:", string)
print("Largest number in the list is", large, end=" ")
print("which was found at index", index)
