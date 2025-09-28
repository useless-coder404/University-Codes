input1 = input("Enter a sentence: ").strip()
input2 = eval(input("Enter special characters: ").strip())

words = []
for w in input1.split():
    w = w.strip(".")
    words.append(w)

print("Words in the given String:", words)

dict_1 = {}

for word in words:
    ascii_sum = 0
    for ch in word:
        ascii_sum += ord(ch)
    idx = ascii_sum % len(input2)
    key = input2[idx]

    if key not in dict_1:
        dict_1[key] = [word]
    else:
        if word not in dict_1[key]:
            dict_1[key].append(word)

print("Answer:", dict_1)
