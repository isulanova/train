n = int(input())
requests = []
for i in range(n):
    requests.append(list(map(int, input().split())))


def parser(number):
    str_num = str(number)
    sum = 0
    for s in str_num:
        sum += int(s)
    #print(sum)
    return sum



for pair in requests:
    number = 1
    for i in range(pair[0], pair[1]+1):
        number *= i
    parser(number)
    while (number > 9):
        number = parser(number)
    print(number)