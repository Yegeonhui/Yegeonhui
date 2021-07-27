import sys
t=int(input())
for i in range(t):
    n=int(input())
    arr=[0 for i in range(n)]
    count=1
    for j in range(n):
        arr[j]=list(map(int,sys.stdin.readline().split()))
    arr.sort()
    min=arr[0][1]
    for i in range(1,n):
        if arr[i][1]<min:
            min=arr[i][1]
            count+=1 
    print(count)
    