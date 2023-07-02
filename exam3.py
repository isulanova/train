length = int(input())
str = input()
str_with_nums = []
s = ""
last_entr = -1
for i in range(len(str)):
    s_new = str[i]
    if s != s_new:
        if len(str_with_nums) > 0 and str_with_nums[-1] != last_entr:
            str_with_nums.append(last_entr)
        str_with_nums.append(s_new)
        str_with_nums.append(i+1)
        s = s_new
    if s == s_new:
        last_entr = i+1
k = 0
letter_list = []
result = length
res_len = length
flag = 1
for i in range(len(str_with_nums)):
    if isinstance(str_with_nums[i], int) != True: #Если буква
        k += 1
        if k < 4:
            letter_list.append(str_with_nums[i])
        if k == 4:
            letter_list.append(str_with_nums[i])
            i += 1
            letter_list.append(str_with_nums[i])
            if len(set(letter_list)) == len(letter_list):
                flag = 0
                if (isinstance(letter_list[2], int)):
                    beg = letter_list[2]
                else:
                    beg = letter_list[1]
                if (isinstance(letter_list[-2], int)):
                    end = letter_list[-2]
                else:
                    end = letter_list[-1]
                res_len = end-beg+1
                if res_len < result:
                    result = res_len
            letter_list.pop(0)
            if isinstance(letter_list[1], int):
                for j in range(2):
                    letter_list.pop(0)
            else:
                letter_list.pop(0)
            k -=1
    else:
        if letter_list[-1] != str_with_nums[i]:
            letter_list.append(str_with_nums[i])
if flag:
    print(-1)
else:
    print(result)


