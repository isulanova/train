nums = list(map(int, input().split()))
sqrt1 = nums[0:2]
sqrt2 = nums[2:]
sqrt1.sort()
sqrt2.sort()
if (sqrt1[0]<=sqrt2[0] and sqrt1[1]<=sqrt2[1]) or (sqrt2[0]<=sqrt1[0] and sqrt2[1]<=sqrt1[1]):
    if sqrt2[0]<=sqrt1[0] and sqrt2[1]<=sqrt1[1]:
        nums = sqrt1[0:2]
        sqrt1 = sqrt2[0:2]
        sqrt2 = nums[0:2]
    x1 = sqrt2[0]
    y1 = sqrt1[1] + sqrt2[1]
    x2 = sqrt2[1]
    y2 = sqrt1[0] + sqrt2[0]
    x3 = sqrt1[0] + sqrt2[1]
    y3 = max(sqrt1[1], sqrt2[0])
    if x1*y1 <= x2*y2 and x1*y1 <= x3*y3:
        print(x1, y1)
    elif x2*y2 <= x1*y1 and x2*y2 <= x3*y3:
        print(x2, y2)
    else:
        print(x3, y3)
else:
    x = max(sqrt1[1], sqrt2[1])
    y = sqrt1[0] + sqrt2[0]
    print(x, y)
