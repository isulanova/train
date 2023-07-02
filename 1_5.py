nums = list(map(int, input().split()))
n = nums[2]/(nums[4] + (nums[3]-1)*nums[1])
P = 0
if int(n) != n:
    n = int(n) + 1
if nums[2] == 1 and nums[3] == 1:
    P1 = 0
else:
    P = nums[0]/(n*nums[1])
    if int(P) != P:
        P = int(P) + 1
    K_new = nums[0] - ((P - 1) * n * nums[1])
if nums[1] == 1:
    N = 1
else:
    N = K_new/n
    if int(N) != N:
        N = int(N) + 1
if P != 0 and n == 1 and P != nums[0]:
    P = N = -1
print(P, N)