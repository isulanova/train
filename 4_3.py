dict = {}
temp = []
with open("input.txt", "r") as f:
    for line in f:
        for i in range(len(line)):
            if line[i] != ' ' and line[i] != '\n':
                temp.append(line[i])
            if line[i] == ' ' or line[i] == '\n' or i == len(line) - 1:
                word = ''.join(temp)
                if len(word) > 0:
                    if word not in dict:
                        dict[word] = 1
                    else:
                        dict[word] += 1
                temp = []
maximum = max(dict.values())
res = []
for word in dict:
    if dict[word] == maximum:
        res.append(word)
res.sort()
print(res[0])