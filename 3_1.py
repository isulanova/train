nums = list(map(int, input().split()))
size = 100
res = [[] for _ in range(size)]
count = 0
for i in range(len(nums)):
    if nums[i] not in res[nums[i] % size]:
        res[nums[i] % size].append(nums[i])
        count += 1
print(count)