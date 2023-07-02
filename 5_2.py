nums = list(map(int, input().split()))
cars = list(map(int, input().split()))
diffs = {}
sum = 0
count = 0
res = 0
for i in range(nums[0]):
    sum += cars[i]
    if sum == nums[1]:
        res += 1
    if sum - (sum // nums[1])*nums[1] not in diffs:
        diffs[sum - (sum // nums[1])*nums[1]] = [sum]
    else:
        diffs[sum - (sum // nums[1])*nums[1]].append(sum)
#print(diffs)
for diff in diffs:
    if len(diffs[diff]) > 1:
        for i in range(1, len(diffs[diff])):
            if diffs[diff][i] - diffs[diff][i-1] == nums[1]:
                res += 1
print(res)

