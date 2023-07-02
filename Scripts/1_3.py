nums = []
for i in range(4):
    nums.append(input())

def parse(str):
    res = []
    if str[0] == '+' and str[1] == '7':
        res.append('8')
        for i in range(2, len(str)):
            if str[i].isdigit():
                res.append(str[i])
    else:
        for i in range(len(str)):
            if str[i].isdigit():
                res.append(str[i])
    if len(res) == 7:
        res = ['8', '4', '9', '5'] + res
    if len(res) == 11:
        return(res)
    else:
        return 1
nums_res = []
for i in range(4):
    if parse(nums[i]) != 1:
        nums_res.append(parse(nums[i]))
if len(nums_res) == 4:
    for i in range(1, 4):
        if nums_res[i] == nums_res[0]:
            print("YES")
        else:
            print("NO")

