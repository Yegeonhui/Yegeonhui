import sys
a,b,c=map(int,sys.stdin.readline().split())

def sol(a,b,c,sum):
    if b==0:
        return 0
    if b==1:
        print(sum*a%c)
    if b%2==1:
        sum*=a
        sol((a*a)%c,b//2,c,sum)
    elif b%2==0:
        sol((a*a)%c,b//2,c,sum)
sum=1
sol(a,b,c,sum)
