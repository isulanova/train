nums = []
for i in range(3):
    nums.append(int(input()))
if len(nums) != 3:
    print()
else:
    if nums[0] <= 0 or nums[1] <= 0 or nums[2] <= 0:
        print()
    else:
        k = 0
        all_nums = sum(nums)
        for side in nums:
            if (all_nums - side) > side:
                k += 1
        if k == 3:
            print("YES")
        else:
            print("NO")