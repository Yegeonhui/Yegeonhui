n=int(input())
arr=[0,0,1,1]
for i in range(4,n+1):
    arr.append(arr[i-1]+1)
    if i%2==0:
        arr[i]=min(arr[i//2]+1,arr[i])
    if i%3==0:
        arr[i]=min(arr[i//3]+1,arr[i])

print(arr[n])
