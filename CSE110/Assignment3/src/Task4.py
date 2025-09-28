total = 0
for num in range(1, 601):
    if (num % 7 == 0 or num % 9 == 0) and not (num % 7 == 0 and num % 9 == 0):
        total += num
print(total)
