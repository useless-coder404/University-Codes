hour = int(input())
if (hour < 0 or hour > 23):
    print("Wrong time")
elif (hour > 0 and hour < 23):
    if (hour >= 4 and hour <= 6):
        print("Breakfast")
    elif (hour >= 12 and hour <= 13):
        print("Lunch")
    elif (hour >= 16 and hour <= 17):
        print("Snacks")
    elif (hour >= 19 and hour <= 20):
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Midnight snack")
