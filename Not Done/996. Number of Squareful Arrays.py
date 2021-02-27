
"""
Not Done
"""
from itertools import permutations
import math
arr=list(map(int,input().split()))
res=permutations(arr)
res2=[]
for i in res:
    ans=[i[j] for j in range(0,len(i)) if j%2==0]
    root=math.sqrt(sum(ans))
    if int(root + 0.5) ** 2 == sum(ans):
        print(sum(ans), "is a perfect square")
        if reversed(ans) not in res2:
            res2.append(ans)
    else:
        print(sum(ans), "is not a perfect square")
print(list(set(map(tuple,sorted(res2)))))



