import heapq
n=int(input())
arr=[]
for i in range(n):
    heapq.heappush(arr,int(input()))
result=0
while len(arr)>1:
    tmp=heapq.heappop(arr)+heapq.heappop(arr)
    print(tmp,arr)
    result+=tmp
    heapq.heappush(arr,tmp)
print(result)