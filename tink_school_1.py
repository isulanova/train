n = int(input())
if n == 1:
    print(0)
else:
    costs = [0]
    need = [0]
    for i in range(0, n):
        need.append(need[-1] + (1+2*i)**2)
        if i != 0:
            cub = (2*(i+1)-1)**3
            costs.append(cub - need[-1])
    print(*costs, sep=" ")




