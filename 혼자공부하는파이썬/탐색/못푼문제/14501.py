n=int(input())
arr=[]
result=[0 for i in range(n)]
print(result)
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n-1,-1,-1):
    if arr[i][0]+i>n:
        if i!=n-1:
            result[i]=result[i+1]
        continue
    else:
        if i==n-1:
            result[i]=arr[i][1]
        elif i+arr[i][0]==n:
            result[i]=max(arr[i][1],result[i+1])
        else:
            result[i]=max(arr[i][1]+result[i+arr[i][0]],result[i+1])

print(result[0])

