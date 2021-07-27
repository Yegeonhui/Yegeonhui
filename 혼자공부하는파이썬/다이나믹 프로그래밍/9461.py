t=int(input())
for i in range(t):
    n=int(input())
    dp=[1 for i in range(n+5)]
    dp[3]=2
    dp[4]=2
    for j in range(5,n+5):
        dp[j]=dp[j-1]+dp[j-5]
    print(dp)
    print(dp[n-1])
