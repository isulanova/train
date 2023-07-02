nums = list(map(int, input().split()))
cars = list(map(int, input().split()))
res = 0
if nums[1] == 1:
    for i in range(nums[0]):
        if cars[i] == 1:
            res += 1
else:
    diffs = {}
    sum = 0
    for i in range(nums[0]):
        sum += cars[i]
        if sum % nums[1] == 0:
            res += 1
            sum = 0
        if sum % nums[1] not in diffs:
            diffs[sum % nums[1]] = 0
        diffs[sum % nums[1]] += 1
    for num in diffs:
        if num != 0 and diffs[num] > 1:
            res += 1
print(diffs)
print(res)