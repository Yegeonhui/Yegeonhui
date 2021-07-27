A=int(input())
N=list(map(int,input().split()))
MAX=max(N)
AVG=0
for i in range(A):
    N[i]=N[i]/MAX*100

AVG=sum(N)/A
print(AVG)