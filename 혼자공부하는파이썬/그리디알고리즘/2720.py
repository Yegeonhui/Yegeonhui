t=int(input())
for i in range(t):
    c=int(input())
    arr=[0 for i in range(4)]
    while c>0:
        if c>=25:
            arr[0]=c//25
            c-=c//25*25
        elif c>=10:
            arr[1]=c//10
            c-=c//10*10
        elif c>=5:
            arr[2]=c//5
            c-=c//5*5
        else:
            arr[3]=c//1
            c-=c//1*1
    print(*arr)