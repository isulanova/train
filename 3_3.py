temp = list(map(int, input().split()))
n, m = temp[0], temp[1]
anya = []
borya = []
temp = []
for i in range(n+m):
    temp.append(int(input()))
anya = set(temp[:n])
borya = set(temp[n:])
common = list(set.intersection(anya, borya))
print(len(common))
common.sort()
print(*common, sep=" ")
anya_unique = list(set(anya - set(common)))
print(len(anya_unique))
anya_unique.sort()
print(*anya_unique, sep=" ")
borya_unique = list(set(borya - set(common)))
print(len(borya_unique))
borya_unique.sort()
print(*borya_unique, sep=" ")
