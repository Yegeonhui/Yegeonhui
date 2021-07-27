import sys
n,k=map(int,sys.stdin.readline().split())
p=1000000007
fac=[1]*(n+1)
for i in range(1,n+1):
    fac[i]=fac[i-1]*i%p
a=fac[n]%p
b=fac[n-k]*fac[k]%p
index=p-2
sum=1
while index>0:
    if index%2==1:
        sum=sum*b%p
    b=b*b%p
    index=index//2
b=sum%p
print(a*b%p)