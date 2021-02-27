"""
The two pointers pattern requires the array to be sorted, so we do that first. As our BCR is O(n2)O(n2), the sort operation would not change the overall time complexity.
"""
arr = [-1,2,1,-4]
target = 1
diff =float('inf')
arr.sort()
for i in range(len(arr)):
    si=i+1
    ei=len(arr)-1
    while si<ei:
        s=arr[i]+arr[si]+arr[ei]
        ##If the absolute difference between sum and target is smaller than the absolute value of diff:
        if abs(target-s)<abs(diff):
            diff=target-s
        if s<target:
            si+=1
        else:
            ei-=1
    if diff == 0:
        break
print(target-diff)
