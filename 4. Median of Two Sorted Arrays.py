import statistics
nums1 = [1,3]
nums2 = [2]
res=statistics.median(sorted(nums1+nums2))
print(res)
