t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    imp=list(map(int,input().split()))
    arr=[]
    for i in imp:
        arr.append(i)
    result=[0 for _ in range(n)]
    que=[i for i in range(n)]
    count=1
    while que:
        if imp[que[0]]==max(arr):
            arr.remove(max(arr))
            result[que.pop(0)]=count
            count+=1
        else:
            que.append(que.pop(0))
    print(result[m])