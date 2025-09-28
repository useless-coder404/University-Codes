hour = int(input())
if hour >= 0 and hour <= 40:
    salary = 200 * hour
    print(salary)
elif hour < 0:
    print("Hour cannot be negative")
elif hour > 168:
    print("Impossible to work more than 168 hours weekly")
else:
    salary = 8000 + (hour - 40) * 300
    print(salary)
