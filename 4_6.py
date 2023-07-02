bd = {}
with open("input.txt", "r") as f:
    for temp in f:
        if temp != '\n':
            dict = {}
            word1 = temp[0:temp.find(' ')]
            temp = temp[temp.find(' ')+1:]
            word2 = temp[0:temp.find(' ')]
            word3 = temp[temp.find(' ')+1:]
            dict[word2] = int(word3)
            if word1 not in bd:
                bd[word1] = dict
            else:
                if word2 not in bd[word1]:
                    bd[word1][word2] = int(word3)
                else:
                    bd[word1][word2] += int(word3)

    for name in sorted(bd):
        print(name + ":")
        for item in sorted(bd[name]):
            print(item, bd[name][item])

# 23634002 27511457 000.py