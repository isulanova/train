a = list(map(int, input().split()))
for i in range(len(a)-1):
    print(list((lambda x, y: x > y, a[i], a[i+1])))


