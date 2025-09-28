quantity = int(input())
num = int(input())
maximum = minimum = total = num

for i in range(quantity - 1):
    num = int(input())
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    total += num

average = total / quantity
print("Maximum", maximum)
print("Minimum", minimum)
print("Average is", average)
