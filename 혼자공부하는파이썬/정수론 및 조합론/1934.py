t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    for i in range(1,max(a,b)+1):
        if a%i==0 and b%i==0:
            count=i
    print(a*b//count)