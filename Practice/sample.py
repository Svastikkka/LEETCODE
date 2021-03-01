import math
def findRestaurants(allLocations, numRestaurants):
    # Write your code here
    dict={}
    for i in allLocations:
        dict[math.sqrt((i[0]*i[0])+(i[1]*i[1]))]=i
    #print(dict)
    #print(numRestaurants)
    res=[]
    for i in range(numRestaurants):
		res.append(min(dict.values()))
    return res
res=[[1,-3],[1,2],[3,4]]
print(findRestaurants(res,1))