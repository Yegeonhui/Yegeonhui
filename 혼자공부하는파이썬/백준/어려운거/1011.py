T=int(input())

for i in range(T) :
    x, y=map(int, input().split())
    k=y-x
    a=int(k**0.5)
    ans=0
    if(a*(a+1)<k<=(a+1)**2) : ans=2*a+1
    elif(a**2<k<=a*(a+1)) : ans=2*a
    else : ans=2*a-1
    print(ans)
