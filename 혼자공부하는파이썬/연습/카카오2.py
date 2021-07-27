from collections import deque
def bfs(arr,i,j):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque()
    que.append([i,j])
    visited=[[100 for _ in range(5)]for _ in range(5)]
    visited[i][j]=1
    while que:
        x,y=que.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==100 and arr[nx][ny]!="X":
                visited[nx][ny]=1
                que.append([nx,ny])
    for a in range(5):
        for b in range(5):
            if arr[a][b]=="P":
                if visited[a][b]==1:
                    if abs(i-a)+abs(j-b)>2 or abs(i-a)+abs(j-b)==0:
                        continue
                    else:
                        return False
                else:
                    continue
    return True

def solution(places):
    result=[]
    for x in places:
        flag=True
        arr=[]
        for i in x:
            arr.append(list(i))
        for i in range(5):
            for j in range(5):
                if arr[i][j]=="P":
                    if bfs(arr,i,j):
                        flag=True
                    else:
                        flag=False
                        break
        if flag:
            result.append(1)
        else:
            result.append(0)
    return result
    
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))