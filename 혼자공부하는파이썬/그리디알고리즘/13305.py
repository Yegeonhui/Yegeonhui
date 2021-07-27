n=int(input())
dis=list(map(int,input().split()))
cost=list(map(int,input().split()))
cost.pop(-1)
result=0
while len(cost)!=0:
    cheap=min(cost)
    cheap_index=cost.index(cheap)
    result+=cheap*sum(dis[cheap_index:len(cost)])
    del cost[cheap_index :]
print(result)