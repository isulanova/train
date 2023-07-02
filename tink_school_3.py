temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
q = temp[2]
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

commands = []
for i in range(q):
    commands.append(list(map(int, input().split())))

for command in commands:
    temp = command
    y = temp[0] - 1
    x = temp[1] - 1
    k = temp[2]
    count = 0
    for y0 in range(n):
        if y0 != y:
            if abs(matrix[y0][x] - matrix[y][x]) <= k:
                count += 1
    for x0 in range(m):
        if x0 != x:
            if abs(matrix[y][x0] - matrix[y][x]) <= k:
                count += 1
    print(count)