n,k,i=map(int,input().split())
count=0
while n!=1:
    n=(n+1)//2 
    count+=1
    k=(k+1)//2
    i=(i+1)//2
    if k==i:
        break 
if k==i:
    print(count)
else:
    print(-1)    

