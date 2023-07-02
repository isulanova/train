a = int(input())
b = int(input())
n = int(input())
m = int(input())
min_t = []
max_t = []
max_t.append(n + a * (n + 1))
max_t.append(m + b * (m + 1))
min_t.append(n + a * (n - 1))
min_t.append(m + b * (m - 1))
print(min_t, max_t)
if (max_t[0] >= min_t[1]) and (max_t[1] >= min_t[0]):
    print(max(min_t), min(max_t))
else:
    print(-1)

