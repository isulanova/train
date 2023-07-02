nums1, nums2 = set(map(int, input().split())), set(map(int, input().split()))
res = list(set.intersection(nums1, nums2))
res.sort()
print(*res, sep=' ')