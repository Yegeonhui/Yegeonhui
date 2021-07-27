n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
result=[]
for i in range(n):
    count=1
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count+=1
    result.append(count)        
print(*result)