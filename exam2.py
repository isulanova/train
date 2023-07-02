a = list(map(int, input().split()))
if ((a[0] * a[2]) % a[1]) == 0:
    minutes = (a[0] * a[2]) // a[1]
else:
    minutes = (a[0] * a[2]) // a[1] + 1
print(minutes)