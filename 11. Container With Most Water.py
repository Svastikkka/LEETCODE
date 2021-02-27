"""
 Two Pointer Approach
"""

def maxArea(height):
    maxArea=0
    left=0
    right=len(height)-1
    while left<right:
        width=abs(left-right)
        if height[left]<height[right]:
            res=width*height[left]
            left+=1
        else:
            res=width*height[right]
            right-=1
        if res>maxArea:
            maxArea=res
    return maxArea



arr=[1,8,6,2,5,4,8,3,7]
print(maxArea(arr))
