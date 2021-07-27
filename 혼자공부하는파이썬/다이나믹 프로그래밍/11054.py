n=int(input())
arr1=list(map(int,input().split()))
arr2=list(reversed(arr1))
dp1=[0 for i in range(n)]
dp2=[0 for i in range(n)]
result=0
for i in range(1,n):
    for j in range(i):
        if arr1[i]>arr1[j]:
            dp1[i]=max(dp1[i],dp1[j]+1)
        if arr2[i]>arr2[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)
for i in range(n):
    result=max(result,dp1[i]+dp2[n-i-1])
print(result+1)