n,m=map(int,input().split())
arr=[[0] for i in range(n)]
for i in range(n):
    arr[i]=list(map(str,input()))
result=[]

def sol(x,y):
    chess=arr[x][y]
    count=0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                if arr[i][j]!=chess:
                    count+=1
            else:
                if arr[i][j]==chess:
                    count+=1
    return min(count,64-count)

for i in range(n-7):
    for j in range(m-7):
        result.append(sol(i,j))

print(min(result))