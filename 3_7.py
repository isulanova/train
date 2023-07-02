n = int(input())
res = []
for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] < n and temp[1] < n:
        if sum(temp) == n - 1:
            res.append(temp[0] + 1)
#print(res)
result = list(set(res))
print(len(result))
