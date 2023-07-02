nums = []
i = int(input())
while i != -2000000000:
    nums.append(i)
    i = int(input())
def ascending(L):
    return all(x<y for x, y in zip(L, L[1:]))

def constant(L):
    return all(x==y for x, y in zip(L, L[1:]))

def weakly_ascending(L):
    return all(x<=y for x, y in zip(L, L[1:]))

def descending(L):
    return all(x>y for x, y in zip(L, L[1:]))

def weakly_descending(L):
    return all(x>=y for x, y in zip(L, L[1:]))

if constant(nums):
    print("CONSTANT")
elif ascending(nums):
    print("ASCENDING")
elif weakly_ascending(nums):
    print("WEAKLY ASCENDING")
elif descending(nums):
    print("DESCENDING")
elif weakly_descending(nums):
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")

'''
nums = list(map(int, input().split()))
k = 0
for i in range(len(nums) - 1):
    if nums[i] < nums[i+1]:
        k += 1
if k+1 == len(nums):
    print("YES")
else:
    print("NO")
'''