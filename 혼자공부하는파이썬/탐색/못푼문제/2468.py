from collections import deque
n=int(input())
arr=[0 for i in range(n)]
h=0
result_arr=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    arr[i]=list(map(int,input().split()))
    h=max(h,max(arr[i]))
def bfs(a,b):
    que=deque()
    que.append([a,b])
    water[a][b]=1
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if water[nx][ny]==0:
                    water[nx][ny]=1
                    que.append([nx,ny])
                    
for i in range(h+1):
    result=0
    water=[[0 for i in range(n)] for i in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k]<=i:
                water[j][k]=1
    for j in range(n):
        for k in range(n):
            if water[j][k]==0:
                bfs(j,k)
                result+=1
    result_arr.append(result)
print(max(result_arr))