num = int(input())
while (num != 0):
    remainder = num % 10
    num = num // 10
    if (num == 0):
        print(remainder, end=" ")
    else:
        print(remainder, end=",")
