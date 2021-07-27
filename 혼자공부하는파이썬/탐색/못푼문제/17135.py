from itertools import combinations
from copy import deepcopy
n,m,d=map(int, input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input().split())))
 
def shoot(y,position,s_board):
    for D in range(1,d+1):
        for left in range(D,-1,-1):
            height=D-left
            if height>0 and 0<=y-height<n and 0<=position-left<m and s_board[y - height][position-left]==1:
                print(height,position,y,left)
                return (y-height,position-left)
        for right in range(1,D+1,1): 
            height=D-right
            if height>0 and 0<=y-height<n and 0<=position+right<m and s_board[y-height][position+right]==1:
                return (y-height,position+right)
    return None
 
def simulation(positions):
    s_board=deepcopy(board)
    killed_amount = 0
    for y in range(n,0,-1):
        killed=[]
        for position in positions:
            killed_enemy=shoot(y,position,s_board)
            if killed_enemy is not None:
                killed.append(killed_enemy)
        for killed_enemy in killed:
            if s_board[killed_enemy[0]][killed_enemy[1]]==1:
                s_board[killed_enemy[0]][killed_enemy[1]]=0
                killed_amount+=1
    return killed_amount

max_v=0
for i in combinations(range(m),3):
    max_v=max(max_v,simulation(i))
print(max_v)