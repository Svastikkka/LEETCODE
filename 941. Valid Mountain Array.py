def solution(arr):
    i=1
    while i<len(arr) and arr[i]>arr[i-1]:
        i+=1
    while i<len(arr) and arr[i]<arr[i-1]:
        i+=1

    return i==len(arr)
arr = [0,3,2,1]
print(solution(arr))