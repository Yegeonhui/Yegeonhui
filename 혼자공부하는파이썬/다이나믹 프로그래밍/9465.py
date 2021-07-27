t=int(input())
for i in range(t):
    n=int(input())
    dp1=[0]+list(map(int,input().split())) 
    dp2=[0]+list(map(int,input().split())) 
    for i in range(2,n+1):
        dp1[i]+=max(dp2[i-2],dp2[i-1])
        dp2[i]+=max(dp1[i-2],dp1[i-1])
    print(max(dp1[-1],dp2[-1]))