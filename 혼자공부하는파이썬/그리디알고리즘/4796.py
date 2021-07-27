cnt=0
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    if v%p<l:
        result=v//p*l+v%p
    else:
        result=v//p*l+l
    cnt+=1
    print("Case ",cnt,": ",result,sep="")
    