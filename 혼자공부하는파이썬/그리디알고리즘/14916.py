n=int(input())
count=0
while n>0:
    if n%5==0:
        n-=5
    elif n%2==0:
        n-=2
    elif n%5!=0 or n%2!=0:
        n-=5
    count+=1
if n==0:
    print(count)    
else:
    print(-1)