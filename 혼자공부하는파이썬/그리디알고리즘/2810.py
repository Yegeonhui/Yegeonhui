n=int(input())
people=list(map(str,input()))
count_l=0
count_s=0
for i in people:    
    if i=="L":
        count_l+=1
    else:
        count_s+=1
if n==1:
    print(1)
elif count_s==n:
    print(n)
else:
    count_ll=count_l//2
    result=n-(count_l-count_ll-1)
    print(result)