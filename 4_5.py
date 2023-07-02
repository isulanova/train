n = int(input())
dict = {}
temp = []
for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] not in dict:
        dict[temp[0]] = [temp[1]]
    else:
        dict[temp[0]].append(temp[1])
blocks = sorted(dict.keys(), reverse=True)
res = max(dict[blocks[0]])
for i in range(1, len(blocks)):
    if blocks[i-1] <= blocks[i]:
        break
    else:
        res += max(dict[blocks[i]])
print(res)