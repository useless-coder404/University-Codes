def rem_duplicate(input_tuple):
    a_list = []
    for i in input_tuple:
        if i not in a_list:
            a_list.append(i)
    unique_tuple = tuple(a_list)
    return unique_tuple


input_tuple = ("Hi", 1, 2, 3, 3, "Hi", "a", "a", [1, 2])
rem_duplicate(input_tuple)
