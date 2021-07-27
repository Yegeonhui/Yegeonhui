n=int(input())
arr=list(map(int,input().split()))
dp=[0 for i in range(n)]
result=-1001
for i in range(n):
    dp[i]=max(dp[i-1]+arr[i],arr[i])
    result=max(result,dp[i])
print(dp)
print(result)