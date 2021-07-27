n,c=map(int,input().split())
m=int(input())
arr=[0 for i in range(m)]
for i in range(m):
    arr[i]=list(map(int,input().split()))
arr.sort(key=lambda arr:arr[1])
cap=[c for i in range(n+1)]
result=0
for i in range(m):
    temp=c
    for j in range(arr[i][0],arr[i][1]):
        temp=min(temp,cap[j])
    temp=min(temp,arr[i][2])
    for j in range(arr[i][0],arr[i][1]):
        cap[j]-=temp
    result+=temp
print(result)
