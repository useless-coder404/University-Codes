canvas = int(input())
paint = int(input())
canvas *= 120
paint *= 75
sum = canvas + paint
print("Previous total:", sum)
if (sum >= 0 and sum <= 299):
    price = sum - 0
    print("New total after discount", price)
elif (sum >= 300 and sum <= 499):
    price = sum - 10
    print("New total after discount", price)
elif (sum >= 500 and sum <= 749):
    price = sum - 20
    print("New total after discount", price)
elif (sum >= 750 and sum <= 999):
    price = sum - 50
    print("New total after discount", price)
else:
    price = sum - 150
    print("New total after discount", price)
