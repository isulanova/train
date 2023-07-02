nums = list(map(int, input().split()))
n = input()
res = []
for letter in n:
    if int(letter) not in res:
        res.append(int(letter))
result = list(set(set(res) - set(nums)))
print(len(result))
