nums = list(map(int, input().split()))
if len(nums) == 2:
    print(min(nums), max(nums))
else:
    imax1 = imax2 = imin1 = imin2 = 0
    flag1 = 0
    flag2 = 0
    for i in range(1, len(nums)):
        if nums[i] >= nums[imax1]:
            imax2 = imax1
            imax1 = i
            #print("max ", nums[imax1], nums[imax2])
            flag1 = 1
        elif nums[i] >= nums[imax2]:
            imax2 = i
            #print("max ", nums[imax1], nums[imax2])
        if nums[i] <= nums[imin1]:
            imin2 = imin1
            imin1 = i
            #print("min ", nums[imin1], nums[imin2])
            flag2 = 1
        elif nums[i] <= nums[imin2]:
            imin2 = i
        #print(nums[i])
    if flag1 and flag2:
        if nums[imax1]*nums[imax2] > nums[imin1]*nums[imin2]:
            print(nums[imax2], nums[imax1])
        else:
            print(nums[imin1], nums[imin2])
    elif flag1:
        print(nums[imax2], nums[imax1])
    elif flag2:
        print(nums[imin2], nums[imin1])

"""print(max1, max2, min1, min2)
print(len(nums))"""
#29852 29908
#891 073 737 mine nums 29908 28470 -29943 -29759
#892 813 616 right nums 29908 29852 -29943 -29781