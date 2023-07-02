nums = list(map(int, input().split()))
if len(nums) == 3:
    nums.sort(reverse=True)
    print(nums[0], nums[1], nums[2])
else:
    maxes = nums[:3]
    """print(maxes)
    maxes.sort()
    print(maxes)"""
    maxes.sort()
    max3 = min1 = maxes[0]
    max2 = min2 = maxes[1]
    max1 = min3 = maxes[2]
    """print(max1, max2, max3)
    print(min1, min2, min3)"""
    for i in range(3, len(nums)):
        if nums[i] >= max1:
            max3 = max2
            max2 = max1
            max1 = nums[i]
        elif nums[i] >= max2:
            max3 = max2
            max2 = nums[i]
        elif nums[i] >= max3:
            max3 = nums[i]
        if nums[i] <= min1:
            min3 = min2
            min2 = min1
            min1 = nums[i]
        elif nums[i] <= min2:
            min3 = min2
            min2 = nums[i]
        elif nums[i] <= min3:
            min3 = nums[i]
    if max1*max2*max3 >= abs(min1*min2*min3):
        print(max1, max2, max3)
    else:
        print(min1, min2, min3)


