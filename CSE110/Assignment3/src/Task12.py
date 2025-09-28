num = int(input())
count = 0
temp = num

while (temp != 0):
    temp //= 10
    count += 1

divider = 10 ** (count - 1)

while (divider != 0):
    digit = num // divider
    num %= divider
    divider //= 10
    if (num == 0):
        print(digit, end=" ")
    else:
        print(digit, end=",")
