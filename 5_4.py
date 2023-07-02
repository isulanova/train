nums = list(map(int, input().split()))
vars = list(map(int, input().split()))
j = 1
res = 0
i = 0
n = nums[0]
while i < n:
    while j < n and vars[j] - vars[i] <= nums[1]:
        j += 1
    res += n - j
    vars.pop(0)
    n -= 1
print(res)