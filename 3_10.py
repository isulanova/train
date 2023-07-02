nums = list(map(int, input().split()))
coords = []
for i in range(nums[2]):
    temp = list(map(int, input().split()))
    if i > nums[2] - 3:
        coords.append(temp)
coord1 = []
coord2 = []
for i in range((-1) * nums[1], nums[1] + 1):
    if i <= 0:
        for j in range(0, nums[1] + 1):
            temp1 = []
            temp1.append(coords[0][0] + i)
            temp1.append(coords[0][1] + j)
            s1 = str(temp1[0]) + ',' + str(temp1[1])
            coord1.append(s1)
            temp2 = []
            temp2.append(coords[1][0] + i)
            temp2.append(coords[1][1] + j)
            s2 = str(temp2[0]) + ',' + str(temp2[1])
            coord2.append(s2)
    if i > 0:
        for j in range(nums[1], -1, -1):
            temp1 = []
            temp1.append(coords[0][0] + i)
            temp1.append(coords[0][1] + j)
            s1 = str(temp1[0]) + ',' + str(temp1[1])
            coord1.append(s1)
            temp2 = []
            temp2.append(coords[1][0] + i)
            temp2.append(coords[1][1] + j)
            s2 = str(temp2[0]) + ',' + str(temp2[1])
            coord2.append(s2)

res = set.intersection(set(coord1), set(coord2))
print(res)
print(coord1)
print(coord2)