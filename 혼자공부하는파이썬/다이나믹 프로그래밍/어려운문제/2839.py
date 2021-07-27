n=int(input())
dp=[5001]*(n+1)
dp[0]=0
arr=[3,5]
for i in arr:
	for j in range(i,n+1):
		if dp[j-i]!=5001:
			dp[j]=min(dp[j],dp[j-i]+1)
if dp[n]==5001:
	print(-1)
else:
	print(dp[n])
