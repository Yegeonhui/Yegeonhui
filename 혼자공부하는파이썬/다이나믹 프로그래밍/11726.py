n=int(input())
dp=[0 for i in range(n+2)]
dp[1]=1
dp[2]=2
for i in range(3,n+2):
    dp[i]=dp[i-1]%10007+dp[i-2]%10007
print(dp[n]%10007)