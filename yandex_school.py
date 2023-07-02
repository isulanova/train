amounts = list(map(int, input().split()))
data = [[0]]
temp = []
opt = []


def reset(data, i):
    for j in range(1, amounts[1] + 1):
        data[i][j] = 1
    data[i][0] += 1
    #print(data)
    return data


def disable(data, i, j):
    data[i][j] = 0
    #print(data)
    return data


def count_ra(data):
    temp = []
    for i in range(1, amounts[0] + 1):
        #print('sum = ', sum(data[i]))
        num = (sum(data[i]) - data[i][0]) * data[i][0]
        #print('num = ', num)
        temp.append(num)
    #print('temp = ', temp)
    return temp


for i in range(1, amounts[0] + 1):
    for j in range(amounts[1] + 1):
        if j == 0:
            temp.append(0)
        else:
            temp.append(1)
    data.append(temp)
    temp = []

for i in range(amounts[2]):
    temp = input().split()
    opt.append(temp)

for i in range(amounts[2]):
    #print('opt = ', opt)
    if opt[i][0] == 'DISABLE':
        data = disable(data, int(opt[i][1]), int(opt[i][2]))
    elif opt[i][0] == 'RESET':
        data = reset(data, int(opt[i][1]))
        #print('RESET')
    elif opt[i][0] == 'GETMAX':
        max_ra = max(count_ra(data))
        print(count_ra(data).index(max_ra) + 1)
    elif opt[i][0] == 'GETMIN':
        min_ra = min(count_ra(data))
        print(count_ra(data).index(min_ra) + 1)
