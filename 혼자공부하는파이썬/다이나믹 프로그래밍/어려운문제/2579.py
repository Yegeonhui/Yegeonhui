n=int(input())
arr=[0 for i in range(n+4)]
for i in range(1,n+1):
    arr[i]=int(input())
dp=[0 for i in range(n+4)]
dp[1]=arr[1]
dp[2]=arr[1]+arr[2]
dp[3]=max(arr[1]+arr[3],arr[2]+arr[3])
for i in range(4,n+4):
    dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
print(dp[n])
