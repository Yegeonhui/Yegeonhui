import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
result=0
for i in range(n):
    count=0
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            count+=1
        else:
            break
        result=max(result,count)
print(result)
