nums = list(map(int, input().split()))
if nums[1] >= nums[2]:
    left = 0
    res = 0
    num_of_k = 0
    #i = 0
    while (nums[0] >= nums[1]):
        #i += 1
        left = nums[0] % nums[1]
        num_of_k = nums[0] // nums[1]
        res += (nums[1] // nums[2]) * num_of_k
        #print(i, "res", res)
        left += (nums[1] % nums[2]) * num_of_k
        nums[0] = left
        #print(i, "left", nums[0])
    print(res)
else:
    print(0)
