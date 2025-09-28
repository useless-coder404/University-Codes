n = int(input())
sum = 0
for y in range(1, n+1, 1):
    power = y ** 2
    if (y % 2 == 0):
        sum = sum - power
    else:
        sum = sum + power
print(sum)
