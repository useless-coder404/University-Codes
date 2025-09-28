def function_name(order_items, location="Dhanmondi"):
    sum = 0
    for i in order_items:
        if i in a_dict:
            sum = sum + a_dict[i]
    if location == "Dhanmondi":
        sum = sum + 30
    else:
        sum = sum + 70
    return sum


order_items = input().split(",")
print(f"{order_items}")

location = input()

a_dict = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}

print(function_name(order_items, location))
