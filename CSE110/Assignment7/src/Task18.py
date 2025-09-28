def function_name(start, end, divisor_1, divisor_2):
    sum = 0
    for num in range(start, end):
        if (num % divisor_1 == 0) != (num % divisor_2 == 0):
            sum += num
    return sum


start = int(input())
end = int(input())
divisor_1 = int(input())
divisor_2 = int(input())

print(function_name(start, end, divisor_1, divisor_2))
