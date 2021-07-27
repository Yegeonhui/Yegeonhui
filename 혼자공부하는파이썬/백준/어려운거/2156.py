n=int(input())
arr=[0]
grape=[0 for i in range(n+1)]
for i in range(1,n+1):
    arr.append(int(input()))
for i in range(1,n+1):
    if i==1:
        grape[1]=arr[1]
    elif i==2:
        grape[2]=arr[1]+arr[2]
    else:
        grape[i]=max(arr[i]+grape[i-3]+arr[i-1],arr[i]+grape[i-2],grape[i-1])
print(grape[n])