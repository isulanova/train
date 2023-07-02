dict = {}
temp = []
res = []
with open("input.txt", "r") as f:
    for s in f:
        for i in range(len(s)):
            if s[i] != ' ' and s[i] != '\n':
                temp.append(s[i])
            if s[i] == ' ' or i == len(s)-1 or s[i] == '\n':
                word = ''.join(temp)
                if len(word) > 0 and word != '\n':
                    if word not in dict:
                        dict[word] = 1
                        res.append(0)
                    else:
                        res.append(dict[word])
                        dict[word] += 1
                    temp = []
print(*res, sep=" ")