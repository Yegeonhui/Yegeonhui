count=0
n=int(input())
while n>0:
    if n%5==0:
        n-=5
    elif n%3==0:
        n-=3
    elif n%5!=0 and n%3!=0:
        n-=5
    count+=1
if n==0:
    print(count)
else:
    print(-1)