"""
https://www.youtube.com/watch?v=WKTgajDkVcA&feature=youtu.be
"""
arr='abcc'
res=set()
left=0
right=0
maxSubString=0
while right<len(arr):
    if arr[right] not in res:
        res.add(arr[right])
        maxSubString=max(maxSubString,len(res))
        right+=1
    else:
        res.remove(arr[left])
        left+=1

print(maxSubString)
