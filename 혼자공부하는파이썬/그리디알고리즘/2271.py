n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=int(input())
arr.sort()
k=n
max_value=0
for i in range(n):
    result=arr[i]*k
    if max_value<result:
        max_value=result
    k-=1
print(max_value)
