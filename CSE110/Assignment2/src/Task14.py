d = int(input())
t = int(input())
d = d / 1000
t = t / 3600
v = float(d / t)
print(v, "km/h")
if (v < 60):
    print("Too slow. Needs more changes.")
elif (v >= 60 and v <= 90):
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")
