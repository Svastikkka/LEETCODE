"""
https://www.youtube.com/watch?v=WKTgajDkVcA&feature=youtu.be
"""
# arr='abcc'
# res=set()
# left=0
# right=0
# maxSubString=0
# while right<len(arr):
#     if arr[right] not in res:
#         res.add(arr[right])
#         maxSubString=max(maxSubString,len(res))
#         right+=1
#     else:
#         res.remove(arr[left])
#         left+=1

# Brute force approach
arr='accde'
max_lenght=0
for i in range(len(arr)):
    seen = {}
    length = 0
    for j in range(i,len(arr)):
        if arr[j] in seen:
            break
        length+=1
        seen[arr[j]] = True
        max_lenght=max(length, max_lenght)
print(max_lenght)

# Sliding Window Technique
arr='accde'
L=0
R=0
seen={}
longest=0
while L<len(arr) and R<len(arr):
    current=arr[R]
    if current in seen:
        previous_position=seen[current]
        L=max(L,previous_position+1)
    seen[current]=R
    longest=max(longest,R-L+1)
    R+=1

print(longest)