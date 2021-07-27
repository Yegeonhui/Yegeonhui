n,m=map(int,input().split())
if n==1:
    count=1
elif n==2:
    count=min(4,1+(m-1)//2)
elif m<7:
    count=min(4,m)
else:
    count=5+(m-7)
print(count)
