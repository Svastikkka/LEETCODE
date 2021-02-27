def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
    return nums

arr=list(map(int,input().split()))
k=int(input())
print(rotate(arr,k))