def robotSim(comd,obs):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x=y=di=0

    obstacleSet=set(map(tuple,obs))

    ans=0
    for cmd in comd:
        if cmd is -2: #left
            di=(di-1)%4
        elif cmd is -1: #right
            di=(di+1)%4
        else:
            for i in range(cmd):
                if (x+dx[di],y+dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x * x + y * y)
    return ans
comd=list(map(int,input().split()))
obs=list(map(int,input().split()))
print(robotSim(comd,obs))




