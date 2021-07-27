a,b=map(int,input().split())
count=1
while a<b:
    if b%2==0:
        b//=2
    elif str(b)[-1]=="1":
        b=str(b)
        b=int(b[0:len(b)-1])
    else:
        break
    count+=1

if a==b:
    print(count)
else:
    print(-1)

