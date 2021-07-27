from itertools import combinations
n,s=map(int,input().split())
arr=list(map(int,input().split()))
count=0
        
def sol(x):
    global count
    for i in combinations(arr,x):
        print(i)
        if sum(i)==s:
            count+=1
        
for i in range(1,n+1):
    sol(i)
print(count)


    