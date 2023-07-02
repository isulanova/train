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
    print(word)
    check = []
    temp = []
    check_flag = 1
    for i in range(len(word)):
        if check_flag:
            print("check_flag = ", check_flag)
            need_parse = check_beg(word[i], D)
            print("need_parse = ", need_parse)
            check_flag = 0
            if need_parse:
                if word[i].isalpha() or word[i] == "_" or word[i].isdigit():
                    temp.append(word[i])
                    if i == len(word) - 1 and len(temp) != 0:
                        check.append("".join(temp))
                        temp = []
                    print(word[i])
                else:
                    if len(temp) != 0:
                        #print(temp)
                        check.append("".join(temp))
                        print(check[-1])
                        check_flag = 1
                        temp = []
            else:
                check_flag = 1


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

