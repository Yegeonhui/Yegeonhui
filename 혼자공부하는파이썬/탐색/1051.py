n,m=map(int,input().split())
arr=[list(map(int,input())) for i in range(n)]
min_len=min(n,m)
result_arr=[]
def sol(x,y):
    result=0
    for i in range(1,min_len):
        if 0<=x+i<n and 0<=y+i<m:
            if arr[x][y]==arr[x+i][y]==arr[x][y+i]==arr[x+i][y+i]:
                result=max(result,i)
    return result


for i in range(n):
    for j in range(m):
        result_arr.append(sol(i,j)+1)
side=max(result_arr)
print(side*side)