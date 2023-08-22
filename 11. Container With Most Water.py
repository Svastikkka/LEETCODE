"""
 Two Pointer Approach
"""

def maxArea(height):
    result=0
    left=0
    right=len(arr)-1
    while (left<right):
        width = right-left
        length = min(arr[left],arr[right])
        area=length*width
        result = max(area,result)

        if arr[left]>arr[right]:
            right-=1
        else:
            left+=1
    return result



arr=[1,8,6,2,5,4,8,3,7]
print(maxArea(arr))
