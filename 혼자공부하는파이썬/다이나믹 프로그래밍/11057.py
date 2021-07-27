n=int(input())
dp=[0]+[1 for i in range(0,10)]
for j in range(n-1):
    for i in range(1,11):
        dp[i]=dp[i]%10007+dp[i-1]%10007
print(sum(dp)%10007)