import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
count=0
result=[i for i in range(1,n+1)]
while True:
    if arr==result:
        break
    for i in range(n-1,0,-1):
        if arr[i]-arr[i-1]==1:
            continue
        elif arr[i]<arr[i-1]:
            num=arr[i-1]
            arr.pop(i-1)
            arr.append(num)
            count+=1
            break 
        elif arr[i]>arr[i-1]:
            num=arr[i-1]
            arr.pop(i-1)
            arr.insert(0,num) 
            count+=1
            break
print(count)