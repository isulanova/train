nums = list(map(int, input().split()))
cars = list(map(int, input().split()))
sum = cars[0]
begin = 0
count = 0
for i in range(1, nums[0]):
    #print(cars[i-1], sum)
    if sum == nums[1]:
        count += 1
        sum -= cars[begin]
        begin += 1
    if sum > nums[1]:
        while sum > nums[1]:
            sum -= cars[begin]
            begin += 1
        if sum == nums[1]:
            count += 1
    sum += cars[i]
if sum == nums[1]:
    count += 1
print(count)