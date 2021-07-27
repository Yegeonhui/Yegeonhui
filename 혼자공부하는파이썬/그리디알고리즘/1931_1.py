n=int(input())
arr=[0 for i in range(n)]
count=1
for i in range(n):
    arr[i]=list(map(int,input().split()))
arr.sort(key=lambda x:(x[1],x[0]))
endtime=arr[0][1]
for i in range(1,n):
    if arr[i][0]>=endtime:
        endtime=arr[i][1]
        count+=1
print(count)