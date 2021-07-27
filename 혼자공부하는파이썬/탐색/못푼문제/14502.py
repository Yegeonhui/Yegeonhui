from itertools import combinations
from copy import deepcopy
n,m=map(int,input().split())
arr=[[0 for i in range(m)]for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
virus=[]
empty=[]
answer=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    lab[x][y]=2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and lab[nx][ny]==0:
            dfs(nx,ny)

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            empty.append([i,j])
        elif arr[i][j]==2:
            virus.append([i,j])
for i in combinations(empty,3):
    lab=deepcopy(arr)
    count=0
    for x,y in i:
        lab[x][y]=1
    for i in range(n):
        for j in range(m):
            if lab[i][j]==2:
                dfs(i,j)

    for i in range(n):
        for j in range(m):
            if lab[i][j]==0:
                count+=1
    if answer<count:    
        answer=count

print(answer)