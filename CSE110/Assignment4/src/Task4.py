word = input()
if word[-2:] == "er":
    print(word[0:-2] + "est")
elif word[-3:] == "est":
    print(word)
elif len(word) < 4:
    print(word)
elif len(word) > 3:
    print(word + "er")
else:
    print(word)
