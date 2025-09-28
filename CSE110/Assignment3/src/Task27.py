binary = input()
decimal = 0
for i in range(len(binary)):
    digit = int(binary[len(binary) - 1 - i])
    decimal += digit*(2**i)
print(decimal)
