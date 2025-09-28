inp = input().split(",")
for i in range(len(inp)):
    inp[i] = int(inp[i])
new_list = []
if (len(inp) >= 4):
    new_list = inp[2:-2]
    print(new_list)
else:
    print("Not possible")
