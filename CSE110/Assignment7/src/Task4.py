def function_name(string):
    u_count = 0
    l_count = 0
    for i in string:
        if (ord(i) >= ord("A") and ord(i) <= ord("Z")):
            u_count += 1
        if (ord(i) >= ord("a") and ord(i) <= ord("z")):
            l_count += 1
    print("No. of Uppercase characters:", u_count)
    print("No. of Lowercase characters:", l_count)


string = input()
function_name(string)
