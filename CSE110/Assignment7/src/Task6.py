def convert_days(no_days):
    year = no_days // 365
    month = (no_days % 365) // 30
    day = (no_days % 365) % 30

    print(f"{year} years, {month} months and {day} days")


user_input = int(input())
convert_days(user_input)
