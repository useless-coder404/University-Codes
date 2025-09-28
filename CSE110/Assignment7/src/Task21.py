def individul_bonus_calculation(name, earn, goals, bonus):
    bonus = goals * (bonus / 100 * earn)
    if goals > 30:
        bonus += 10000
    elif 20 <= goals <= 30:
        bonus += 5000
    return bonus


def calculate_total_bonus_for_players(*players):
    for player in players:
        name, earn, goals, bonus = player
        total_bonus = individul_bonus_calculation(name, earn, goals, bonus)
        print(f"{name} earned a bonus of {total_bonus}", end=" ")
        print(f"Taka for {goals} goals.")


players_info = [
    ("Neymar", 1200000, 35, 5),
    ("Jamal", 700000, 19, 8),
    ("Luis", 80000, 25, 10),
]

calculate_total_bonus_for_players(*players_info)
