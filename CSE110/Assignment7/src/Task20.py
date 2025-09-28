def individul_bonus_calculation(name, earn, goals, bonus):
    bonus = goals * (bonus / 100 * earn)
    if goals > 30:
        bonus += 10000
    elif 20 <= goals <= 30:
        bonus += 5000
    return bonus


name = input("Enter the player's name: ")
earn = int(input("Enter the player's monthly earning: "))
goals = int(input("Enter the number of goals scored: "))
bonus = int(input("Enter the bonus percentage: "))

total_bonus = individul_bonus_calculation(name, earn, goals, bonus)

print(f"{name} earned a bonus of {total_bonus} Taka for {goals} goals.")
