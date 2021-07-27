from itertools import combinations
from copy import deepcopy
from collections import deque
n,m=map(int,input().split())
lab=[list(map(int,input().split())) for i in range(n)]
virus=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
answer=100000

def sol(inf,arr):
    que=deque()
    visited=[[0 for i in range(n)] for j in range(n)]
    for vir in arr:
        x,y=vir[0],vir[1]
        que.append((x,y,0))
        visited[x][y]=1
    while que:
        x,y,time=que.popleft() 
        if time>answer:
            break
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if inf[nx][ny]!="-" and visited[nx][ny]==0:
                if inf[nx][ny]=="*" and visited[nx][ny]==0:
                    visited[nx][ny]=1                
                    que.append((nx,ny,time+1))
                    continue
                visited[nx][ny]=1                
                inf[nx][ny]=time+1
                que.append((nx,ny,time+1))
    check(inf)

def check(arr):
	global answer
	temp=0
	for i in range(n):
		for j in range(n):
			if arr[i][j]=="-" or arr[i][j]=="*" or arr[i][j]=="**":
				continue
			if arr[i][j]==0:
				return
			if temp<arr[i][j]:
				temp=arr[i][j]	
	answer=min(temp,answer)

for i in range(n):
    for j in range(n):
        if lab[i][j]==2:
            virus.append((i,j))
        elif lab[i][j]==1:
            lab[i][j]="-"
i=list(combinations(virus,m))
for j in i:
    board=deepcopy(lab)
    no=set(virus)-set(j)
    for vi in j:
        board[vi[0]][vi[1]]="**"
    for vi in no:
        board[vi[0]][vi[1]]="*"
    sol(board,j)
if answer==100000:
	print(-1)
else:
	print(answer)
