def solution(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    for i in range(j,len(nums)):
        nums[i]=0

    return nums

nums = [0,1,0,3,12]
print(solution(nums))
