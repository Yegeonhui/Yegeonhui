n=int(input())
k=int(input())
arr=list(map(int,input().split()))
arr.sort()
arr1=[]
if n==1:
    print(0)
else:
    for i in range(1,n):
        arr1.append(arr[i]-arr[i-1])
    arr1.sort()
    for i in range(k-1):
        arr1.pop()  
    print(sum(arr1))
        


