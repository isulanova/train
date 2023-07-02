"""import time
start_time = time.time()"""
n = int(input())
nums = list(map(int, input().split()))
vas = 0
flag = 1
max = nums[0]
index = 0
vas = 0
for i in range(1, len(nums) - 1):
    if nums[i] > max:
        max = nums[i]
        index = i
        vas = 0
    if nums[i] % 10 == 5:
        if index < i and nums[i] > nums[i + 1]:
            if flag:
                vas = nums[i]
                flag = 0
            else:
                if vas < nums[i]:
                    vas = nums[i]
    #print(i, max, index, vas)
if vas == 0:
    print(0)
else:
    k = 0
    for i in range(n):
        if nums[i] > vas:
            k += 1
    print(k+1)
    #print(vas)
"""end_time = time.time()
print(end_time-start_time)"""