n=int(input())
num=list(map(int,input().split()))
m=int(input())
arr=list(map(int,input().split()))
result=[0 for i in range(n)]
for i in range(n):
    for j in num:
        if num[j]==i:
            result[j]==1
print(result)
            
