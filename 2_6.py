n = int(input())
nums = list(map(int, input().split()))
middle = n//2
count = 0
flag = 0
for i in range(n):
    j = 0
    count = 0
    if (n-i) % 2 == 0:
        middle -= 1
    k = i
    for j in range(n-1, middle, -1):
        #print(nums[k], nums[j])
        if nums[k] == nums[j]:
            count += 1
        k += 1
    middle += 1
    if count == (n-i) // 2:
        if j != k:
            flag = 1
        break
    #print("count = ", count, '(n-i) // 2 = ', (n-i) // 2)
#print(count)
#print(n - count*2)

def pack(n):
    s = []
    for i in range(n, -1, -1):
        # print(nums[i])
        s.append(str(nums[i]))
    print(len(s))
    print(' '.join(s))

if n // 2 == count:
    print(0)
else:
    if count == 0:
        pack(n-2)
        """s = []
        for i in range (n-2, -1, -1):
            #print(nums[i])
            s.append(str(nums[i]))
        print(' '.join(s))"""
    else:
        if flag:
            pack(n - count * 2 - 2)
        else:
            pack(n - count*2 - 1)