t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[0 for i in range(m)]
    for i in range(m):
        arr[i]=list(map(int,input().split()))
    arr.sort(key=lambda arr:(arr[1],arr[0]))
    books=[]
    used=[0]*(n+1)
    count=0
    for start,end in arr:
        for booknum in range(1,n+1):
            if booknum>=start and booknum<=end and used[booknum]==0:
                used[booknum]=1
                count+=1
                break
    print(count)