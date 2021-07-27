from collections import deque
n,m=map(int,input().split())
arr=deque(map(int,input().split()))
count=0
que=deque([])
for i in range(1,n+1):
    que.append(i)
while arr:
    if que[0]==arr[0]:
        arr.popleft()
        que.popleft()
    else:
        if que.index(arr[0])<=len(que)-que.index(arr[0]):
            while que[0]!=arr[0]:
                que.append(que[0])
                que.popleft()
                count+=1
        else:
            while que[0]!=arr[0]:
                que.appendleft(que[-1])
                que.pop()
                count+=1
print(count)