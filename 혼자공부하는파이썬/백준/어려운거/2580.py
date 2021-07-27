sdk=[list(map(int,input().split())) for i in range(9)]
zeros=[(i,j) for i in range(9) for j in range(9) if sdk[i][j]==0]
def solution(i,j):
    arr=[1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if sdk[i][k] in arr:
            arr.remove(sdk[i][k])
        if sdk[k][j] in arr:
            arr.remove(sdk[k][j])
    i//=3
    j//=3
    for p in range(i*3,(i+1)*3):
        for q in range(j*3,(j+1)*3):
            if sdk[p][q] in arr:
                arr.remove(sdk[p][q])
    return arr

flag=False
def dfs(x):
    global flag
    if flag: 
        return
    if x==len(zeros): 
        for row in sdk:
            print(*row)
        flag=True 
        return
    else:    
        (i,j)=zeros[x]
        promising=solution(i,j) 
        for num in promising:
            sdk[i][j]=num 
            dfs(x+1) 
            sdk[i][j]=0 
dfs(0)
