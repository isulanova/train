n = int(input())
commands = []
for i in range(n):
    commands.append(list(map(int, input().split())))
queue = []
begin = 0
length = 0
for command in commands:
    if command[0] == 1:
        queue.append(command[1])
        queue.append(1)
        length += 2
    elif command[0] == 2:
        for i in range(begin, length):
            if i % 2 != 0:
                queue[i] *= 2
    elif command[0] == 3:
        if queue[begin + 1] > 0:
            queue[begin + 1] -= 1
            print(queue[begin])
        else:
            begin += 2
            print(queue[begin])
            queue[begin + 1] -= 1
    #print(queue, length)



