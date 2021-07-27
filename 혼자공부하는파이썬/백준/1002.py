t=int(input())
for i in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dis=((x2-x1)**2+(y2-y1)**2)**0.5
    if r2>r1:
        r1,r2=r2,r1
    if dis==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if r1+r2==dis or r1-r2==dis:
            print(1)
        elif r1+r2>dis and r1-r2<dis:
            print(2)
        else:
            print(0)