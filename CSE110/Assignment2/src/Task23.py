temp = int(input())
degree_C = (temp - 32) * 0.56
rounded_number = round(degree_C, 2)
print(rounded_number, "degrees C")
if (degree_C < 20):
    print("Winter")
elif (degree_C >= 20 and degree_C <= 25):
    print("Autumn")
elif (degree_C > 25 and degree_C < 30):
    print("Spring")
elif (degree_C >= 30):
    print("Summer")
else:
    print("Error")
