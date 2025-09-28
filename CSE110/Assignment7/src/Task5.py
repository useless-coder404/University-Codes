def calculate_tax(age, salary, designation):
    if age < 18 or designation == "president" or salary < 10000:
        tax = 0
    elif 10000 <= salary <= 20000:
        tax = salary * 0.05
    else:
        tax = salary * 0.1
    return tax


age = int(input())
salary = int(input())
designation = input()

calculate_tax(age, salary, designation)

print(calculate_tax(age, salary, designation))
