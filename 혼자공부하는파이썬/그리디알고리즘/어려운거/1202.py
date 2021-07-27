import sys
import heapq
n,k=map(int,sys.stdin.readline().split())
gem=[]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    heapq.heappush(gem,[w,v])
bag=[]
for i in range(k):
    heapq.heappush(bag,int(sys.stdin.readline()))
judge=[]
result=0
for i in range(k):
    capacity=heapq.heappop(bag)
    while len(gem)>0 and capacity>=gem[0][0]:
        w=heapq.heappop(gem)[1]
        heapq.heappush(judge,-w)
    if len(judge)>0:
        result-=heapq.heappop(judge)
print(result)
