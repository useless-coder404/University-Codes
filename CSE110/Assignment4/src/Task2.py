string = input()
index = int(input())
output = string[index::-1] + string[index+1::]
print(output)
