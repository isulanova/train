text = []

with open('input.txt', 'r') as f:
    for line in f:
        #print(line)
        begin = 0
        i = 0
        while i < len(line):
            if line[i] == ' ' or line[i] == '\n':
                if line[begin:i] != '' and line[begin:i] != '\n':
                    text.append(line[begin:i])
                    #print(line[begin:i])
                    if line[i] == '\n':
                        break
                    if line[i+1] != ' ':
                        begin = i + 1
                    else:
                        while line[i] == ' ':
                            i += 1
                        begin = i
            i += 1
res = list(set(text))
print(len(res))
