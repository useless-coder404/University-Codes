user_input = input()
items = user_input.split(",")

a_dict = {}

for item in items:
    key, value = item.strip().split(":")
    a_dict[key.strip()] = value.strip()

total = 0
count = 0
for value in a_dict.values():
    total += int(value)
    count += 1

avg = total / count
print(f"Average is {avg}")
