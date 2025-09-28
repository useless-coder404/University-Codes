def calculator(operator, first_operand, second_operand):
    result = None
    if (operator == "+"):
        result = first_operand + second_operand
    elif (operator == "-"):
        result = first_operand - second_operand
    elif (operator == "*"):
        result = first_operand * second_operand
    elif (operator == "/"):
        result = first_operand / second_operand
    return result


operator = input()
first_operand = float(input())
second_operand = float(input())

result = calculator(operator, first_operand, second_operand)

print(float(result))
