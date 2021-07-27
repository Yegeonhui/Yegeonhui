def mul(a,b):
    if b==0:
        return a
    else:
        return mul(b,a%b)

n=int(input())
m=list(map(int,input().split()))
for i in range(1,n):
    a=mul(m[0]*2,m[i]*2)
    print(m[0]*2//a,"/",m[i]*2//a,sep="")
