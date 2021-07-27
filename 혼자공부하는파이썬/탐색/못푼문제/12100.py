from collections import deque
from copy import deepcopy
n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
answer,q=0,deque()

def sol(count):
    global board, answer
    if count==5:
        for i in range(n):
            answer=max(answer,max(board[i]))
        return
    b=deepcopy(board)
    for k in range(4):
        move(k)
        sol(count+1)
        board=deepcopy(b)

def get(i,j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j]=0

def move(k):
    if k==0: #위
        for j in range(n):
            for i in range(n):
                get(i,j)
            merge(0,j,1,0)
    elif k==1:#아래
        for j in range(n):
            for i in range(n-1,-1,-1):
                get(i,j)
            merge(n-1,j,-1,0)
    elif k==2:
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(i,0,0,1)
    else:
        for i in range(n):
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i,n-1,0,-1)

def merge(i,j,di,dj):
    while q:
        x=q.popleft()
        if not board[i][j]:
            board[i][j]=x
        elif board[i][j]==x:
            board[i][j]=x*2 
            i,j=i+di,j+dj 
        else:
            i,j=i+di,j+dj
            board[i][j]=x  
sol(0)
print(answer)