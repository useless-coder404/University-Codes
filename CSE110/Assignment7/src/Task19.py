def function_name(word):
    a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    emp_list = []

    for i in range(0, len(word)):
        if word[i] not in emp_list:
            emp_list.append(word[i])

    for char in a_list:
        if char not in emp_list:
            return 6
    return 5


user = input()

small = user.lower()
the_word = small.replace(' ', '')

score = function_name(the_word)

for _ in range(score):
    print("PSG will win the Champions League this season")
