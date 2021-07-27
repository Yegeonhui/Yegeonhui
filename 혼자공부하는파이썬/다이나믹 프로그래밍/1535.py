n=int(input())
arr1=[0]+list(map(int,input().split()))
arr2=[0]+list(map(int,input().split()))
dp=[[0 for i in range(101)]for i in range(21)]
for i in range(1,n+1):
    for j in range(1,100):
        if arr1[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-arr1[i]]+arr2[i],dp[i-1][j])

print(dp[n][99])