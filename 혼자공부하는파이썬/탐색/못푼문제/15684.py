n,m,h=map(int,input().split())
table=[[0 for i in range(n+2)] for j in range(h)]
for i in range(m):
    a,b=map(int,input().split())
    table[a-1][b]=1
answer=4

def check(maps):
    for col in range(1,len(maps[0])-2):
        start=col
        for row in range(len(maps)):
            if maps[row][col]==1:
                col+=1
            elif maps[row][col-1]==1:
                col-=1
        if col!=start:
            return False
    return True


def ladder(maps,cnt,limit):
    global answer
    if cnt==limit:
        if check(maps):
            answer=min(answer,limit)
        return 
    for y in range(h):
        for x in range(1,n+2):
            if maps[y][x]!=1 and maps[y][x-1]!=1 and maps[y][x+1]!=1:
                maps[y][x]=1
                ladder(maps,cnt+1,limit)
                maps[y][x]=0

for i in range(4):
    ladder(table,0,i)
    