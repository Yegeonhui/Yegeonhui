n,k=map(int,input().split())
coin=[0 for i in range(n)]
for i in range(n):
    coin[i]=int(input())
count=0
while k!=0:
    for i in reversed(coin):
        if i>k:
            continue
        else:
            count+=k//i
            k-=k//i*i

print(count)