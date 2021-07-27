from collections import deque
from copy import deepcopy
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
cctv=[]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
di=[[0], [[0],[1],[2],[3]], [[0,1],[2,3]], [[0,2],[0,3],[1,2],[1,3]], [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]

MIN=9999999999999999
def dfs(start,map,cctv):
    global MIN
    if start==len(cctv):
        cnt=0
        for y in range(n):
            for x in range(m):
                if map[y][x]==0:
                    cnt+=1
        MIN=min(MIN,cnt)
        return

    num,y,x=cctv[start]
    for dir in di[num]:
        tmp=deepcopy(map)
        for i in dir:
            ny=y+dy[i]
            nx=x+dx[i]
            while 0<=ny<n and 0<=nx<m:
                if tmp[ny][nx]==6:
                    break
                elif tmp[ny][nx]==0:
                    tmp[ny][nx]="#"
                ny+=dy[i]
                nx+=dx[i]
        dfs(start+1,tmp,cctv)

for j in range(n):
    for i in range(m):
        if arr[j][i] not in [0,6]:
            cctv.append([arr[j][i],j,i])
dfs(0,arr,cctv)
print(MIN)