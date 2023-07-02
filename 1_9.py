a, b, c, d, e = [int(input()) for _ in range(5)]
#ab bc ac
if min(a, b) <= min(d, e) and max(a, b) <= max(d, e):
    print("YES")
elif min(c, b) <= min(d, e) and max(c, b) <= max(d, e):
    print("YES")
elif min(a, c) <= min(d, e) and max(a, c) <= max(d, e):
    print("YES")
else:
    print("NO")