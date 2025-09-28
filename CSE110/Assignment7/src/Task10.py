def make_square(number_range):
    start, end = number_range
    dict_1 = {}
    for num in range(start, end + 1):
        dict_1[num] = num ** 2
    return dict_1


number_range = (5, 9)
print(make_square(number_range))
