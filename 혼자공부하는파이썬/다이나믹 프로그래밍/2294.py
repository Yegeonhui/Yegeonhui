n,k=map(int,input().split())
arr=[int(input()) for i in range(n)]
dp=[10001 for i in range(k+1)]
dp[0]=0
for i in arr:
    for j in range(i,k+1):
        if dp[j-i]!=10001:
            dp[j]=min(dp[j],dp[j-i]+1)
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])
print(dp)