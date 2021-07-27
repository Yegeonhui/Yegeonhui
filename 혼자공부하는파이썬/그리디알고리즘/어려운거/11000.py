import sys
import heapq
n=int(sys.stdin.readline())
room=[]
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,sys.stdin.readline().split()))
arr.sort(key=lambda x:x[0])
heapq.heappush(room,arr[0][1])
for i in range(1,n):
    if room[0]<=arr[i][0]:
        heapq.heappop(room)
        heapq.heappush(room,arr[i][1])
    else:
        heapq.heappush(room,arr[i][1])
print(len(room))