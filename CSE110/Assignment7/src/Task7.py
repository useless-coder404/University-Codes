def show_palindrome(num):
    string = ""
    for i in range(1, num+1):
        string += str(i)
    for i in range(num-1, 0, -1):
        string += str(i)
    return string


num = int(input())
print(show_palindrome(num))
