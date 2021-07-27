import sys
import heapq
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    arr.sort()
    tmp=arr[0]+arr[1]
    tmp=heapq.heappop(arr)+heapq.heappop(arr)
    heapq.heappush(arr,tmp)
    heapq.heappush(arr,tmp)
    print(arr)
print(sum(arr))
    