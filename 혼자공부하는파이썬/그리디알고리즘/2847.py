n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=int(input())
tmp=arr[-1]    
result=0
count=0
for i in range(1,n):
    if arr[n-i-1]>=tmp:
        count=arr[n-i-1]-tmp+1
        result+=count
        tmp=arr[n-i-1]-count
    else:
        tmp=arr[n-i-1]
print(result)