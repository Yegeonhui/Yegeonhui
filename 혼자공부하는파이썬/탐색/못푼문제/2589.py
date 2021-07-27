from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[list(map(str,input())) for i in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=0 

def bfs(x,y):
    global m,n
    queue=deque()
    queue.append((x,y))
    res=0
    check=[[0 for i in range(m)] for j in range(n)]
    check[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]=="L" and check[nx][ny]==0: 
                queue.append((nx,ny))
                check[nx][ny]=check[x][y]+1
                res=max(res,check[nx][ny])
    print(check)
    return res-1

for i in range(n):
    for j in range(m):
        if arr[i][j]=="L":
            result=max(result,bfs(i,j))
print(result)
