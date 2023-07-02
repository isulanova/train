nums = list(map(int, input().split()))
cars = list(map(int, input().split()))
sum = 0
begin = 0
count = 0
for i in range(len(cars)):
    sum = 0
    for j in range(i, len(cars)):
        sum += cars[j]
        if sum == nums[1]:
            count += 1
print(count)