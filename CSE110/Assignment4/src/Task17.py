string = input()
character = input()
start = 0
for i in range(len(string)):
    if string[i] == character:
        print(string[start:i])
        start = i + 1
print(string[start:])
