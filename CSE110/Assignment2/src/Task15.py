cgpa = float(input())
credits = int(input())
if (cgpa < 3.80 and credits < 30):
    print("The student is not eligible for a waiver")
elif (cgpa > 3.80 and credits > 30):
    if (cgpa >= 3.80 and cgpa <= 3.89):
        print("The student is eligible for a waiver of 25 percent.")
    elif (cgpa >= 3.90 and cgpa <= 3.94):
        print("The student is eligible for a waiver of 50 percent.")
    elif (cgpa >= 3.95 and cgpa <= 3.99):
        print("The student is eligible for a waiver of 75 percent.")
    elif (cgpa == 4.00):
        print("The student is eligible for a waiver of 100 percent.")
    else:
        print("The student is not eligible for a waiver")
else:
    print("The student is not eligible for a waiver")
