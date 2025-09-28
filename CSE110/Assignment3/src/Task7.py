total = 0
count = 0
for i in range(10):
    num = int(input())
    if (num % 2 != 0):
        total += num
        count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("The total of the odd numbers is", total,
      "and their average is", average)
