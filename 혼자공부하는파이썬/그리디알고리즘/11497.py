t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    result=0
    for j in range(2,n):
        result=max(result,abs(arr[j]-arr[j-2]))
    print(result)