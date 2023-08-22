def solution(arr,limit):
    heavy=len(arr)-1
    light=0
    count=0
    while light<=heavy:
        if arr[heavy]==limit:
            heavy-=1
            count+=1
        if arr[heavy]+arr[light]==limit:
            heavy-=1
            light+=1
            count+=1
        else:
            heavy-=1
            count+=1
    return count

people = [3,5,3,4]
limit = 5
print(solution(people,limit))