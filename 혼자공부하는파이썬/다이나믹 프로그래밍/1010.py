t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    result=1
    result1=1
    for j in range(1,min(m,n)+1):
        result=result*(max(m,n)-j+1)
        result1=result1*j
    print(result//result1)