mark = int(input())
if (mark < 0 or mark > 100):
    print("Invalid")
elif (mark >= 0 and mark <= 100):
    if (mark >= 90):
        print("A")
    elif (mark >= 80 and mark <= 89):
        print("B")
    elif (mark >= 70 and mark <= 79):
        print("C")
    elif (mark >= 60 and mark <= 69):
        print("D")
    elif (mark >= 50 and mark <= 59):
        print("E")
    else:
        print("F")
else:
    print("Invalid")
