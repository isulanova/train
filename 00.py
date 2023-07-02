nums = []
key_words = []
ids = {}
i = 0


def check_beg(s, D):
    if D == "no":
        return s.isalpha()
    else:
        if s.isalpha() or s.isdigit():
            return True
        else:
            return False


def parser(word, D):
    #print(word)
    check = []
    temp = []
    if check_beg(word[0], D):
        i = 0
        while i < len(word):
            if word[i].isalpha() or word[i] == "_" or word[i].isdigit():
                temp.append(word[i])
                if i == len(word) - 1 and len(temp) != 0:
                    check.append("".join(temp))
                    temp = []
            else:
                if len(temp) != 0:
                    #print(temp)
                    check.append("".join(temp))
                    flag = 0
                    while i < len(word) and check_beg(word[i], D) is False:
                        print(word[i])
                        i += 1
                        flag = 1
                    temp = []
                    if flag:
                        i -= 1
            i += 1

    return check

with open("input.txt", "r") as f:
    for line in f:
        if len(nums) == 0:
            nums = list(map(str, line.split()))
        else:
            if i < int(nums[0]):
                key_words.append(line[:len(line)-1])
                i += 1
            else:
                temp = list(map(str, line.split()))
                #print(temp)
                for word in temp:
                    if nums[1] == "no":
                        temp = parser(word.lower(), nums[2])
                    else:
                        temp = parser(word, nums[2])
                    print(temp)
                    #if len(temp) != 0:

