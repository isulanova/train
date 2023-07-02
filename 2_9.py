nums = list(map(int, input().split()))
mins = []
for i in range(nums[2]):
    temp = list(map(int, input().split()))
    mins.append(temp)

def get_neighb(i, j):
    count = 0
    if i == 0:
        left_i = 0
        right_i = 1+1
    elif i == nums[0]-1:
        left_i = i - 1
        right_i = i+1
    else:
        left_i = i - 1
        right_i = i + 2
    if j == 0:
        left_j = 0
        right_j = 1+1
    elif j == nums[1]-1:
        left_j = j - 1
        right_j = j+1
    else:
        left_j = j - 1
        right_j = j + 2
    for k in range(left_i, right_i):
        for g in range(left_j, right_j):
            if k != i or g != j:
                temp = [k+1]
                temp.append(g+1)
                if temp in mins:
                    count += 1
    return count

for i in range(nums[0]):
    for j in range(nums[1]):
        temp = [i+1]
        temp.append(j+1)
        if temp in mins:
            print('*', end='', flush=True)
        else:
            count = str(get_neighb(i, j))
            print(count, end='', flush=True)
        if j != nums[1] - 1:
            print(' ', end='')
    if i != nums[0] - 1:
        print()


