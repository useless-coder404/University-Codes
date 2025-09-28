s = int(input())
if s < 100:
    result = 3000 - 125 * s ** 2
    print(result)
else:
    result = 12000 / (4 + s ** 2 / 14900)
    print(result)
