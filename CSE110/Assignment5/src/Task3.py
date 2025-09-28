lst = []
for i in range(5):
    num = int(input())
    lst.append(num)
print("Printing values from the list in reverse order:")
for i in range(len(lst)):
    print(lst[-i-1])
