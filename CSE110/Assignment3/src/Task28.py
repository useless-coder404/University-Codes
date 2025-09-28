start = int(input())
end = int(input())

prime_numbers = []
perfect_numbers = []

for num in range(start, end + 1):
    is_prime = True
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    divisors = [1]
    sum_divisors = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
            sum_divisors += i

    is_perfect = num == sum_divisors

    if is_prime:
        prime_numbers.append(num)
    if is_perfect:
        perfect_numbers.append(num)

print(f"Between {start} and {end},")
print(f"Found {len(prime_numbers)} prime numbers")
print(f"Found {len(perfect_numbers)} perfect number")
print("Prime numbers:", ", ".join(map(str, prime_numbers)))
print("Perfect numbers:", ", ".join(map(str, perfect_numbers)))
