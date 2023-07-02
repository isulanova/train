n = int(input())
clavs = list(map(int, input().split()))
n_click = int(input())
clicks = list(map(int, input().split()))
for click in clicks:
    clavs[click-1] -= 1
for clav in clavs:
    if clav < 0:
        print("YES")
    else:
        print("NO")