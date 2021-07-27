n,b=map(int,input().split())
arr=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
b=bin(b)[2:]

def matrix_mul(a,b):
    result=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=a[i][k]*b[k][j]
    for i in range(n):
        for j in range(n):
            result[i][j]%=1000
    return result
    
matrix=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            matrix[i][j]=1
result=matrix[:]
for i in range(len(b)):
    if b[-i-1]=="1":
        temp=arr[:]
        while i!=0:
            temp=matrix_mul(temp,temp)
            i-=1
        result=matrix_mul(result,temp)
for row in result:
    print(*row)
