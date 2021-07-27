from itertools import combinations
l,c=map(int,input().split())
arr=list(map(str,input().split()))
arr.sort()

def sol(x):
    count=0
    for i in x:
        if i=="a":
            count+=1
        if i=="e":
            count+=1
        if i=="i":
            count+=1
        if i=="o":
            count+=1
        if i=="u":
            count+=1
    if count>0 and count<l-1:
        print(*x,sep="")

for i in combinations(arr,l):
    sol(i)