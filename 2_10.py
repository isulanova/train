n = int(input())
nums = []
first = [input()]
first.append('')
nums.append(first)
begin = 30
end = 4000
for i in range(n-1):
    temp = list(map(str, input().split()))
    nums.append(temp)
for i in range(1, n):
    f0 = float(nums[i-1][0])
    f1 = float(nums[i][0])
    if nums[i][1] == "closer":
        if f1-f0 > 0:
            if (f0+f1)/2 > begin:
                begin = (f0+f1)/2
        if f1 - f0 < 0:
            if (f0+f1)/2 < end:
                end = (f0+f1)/2
    if nums[i][1] == "further":
        if f1-f0 > 0:
            if (f0+f1)/2 < end:
                end = (f0+f1)/2
        if f1-f0 < 0:
            if (f0+f1)/2 > begin:
                begin = (f0+f1)/2
print(begin, end)