def function(sentence, position):
    removed = ""
    new_string = ""
    for i in range(len(sentence)):
        if (i != 0 and i % position == 0):
            removed += sentence[i]
        else:
            new_string += sentence[i]
    return (new_string, removed)


sentence = input()
position = int(input())

new_string, removed = function(sentence, position)

print(f"{new_string}{removed}")
