n=int(input())
arr=[0]+list(map(int,input().split()))
dp=[0 for i in range(n+1)]
for i in range(n+1):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(arr[i]+dp[j],dp[i])
print(max(dp))