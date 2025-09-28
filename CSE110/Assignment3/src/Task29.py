start = int(input())
end = int(input())
check = int(input())
for num in range(start, end+1):
    products = 1
    for digit in str(num):
        products *= int(digit)
    if (products % check == 0):
        print(products, end=" ")
