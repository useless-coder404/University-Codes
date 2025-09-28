def show_palindromic_triangle(num):
    for i in range(1, num+1):
        for space in range(1, (num-i)+1):
            print(" ", end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
        for j in range(i-1, 0, -1):
            print(j, end=" ")
        print()


num = int(input())
show_palindromic_triangle(num)
