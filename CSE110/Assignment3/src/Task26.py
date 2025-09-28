decimal_num = int(input())
binary_num = ""
while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num //= 2
print(binary_num)
