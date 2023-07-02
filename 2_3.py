n = int(input())
nums = list(map(int, input().split()))
number = int(input())
abses = []
for i in range(len(nums)):
    abses.append(abs(nums[i]-number))
print(nums[abses.index(min(abses))])
