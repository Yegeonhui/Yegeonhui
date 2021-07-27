n,m=map(int,input().split())
a=[[] for i in range(n)]
for i in range(n):
    a[i]=list(map(int,input().split()))
m,k=map(int,input().split())
b=[[] for i in range(m)]
for i in range(m):
    b[i]=list(map(int,input().split()))
result=[[0 for i in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
                result[i][j]+=a[i][l]*b[l][j]
for i in range(n):
    for j in range(k):
        print(result[i][j],end=" ")
    print("")