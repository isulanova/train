n = int(input())
res = []
for i in range(n):
    temp = list(map(int, input().split()))
    res.append(temp[0])
result = list(set(res))
print(len(result))
