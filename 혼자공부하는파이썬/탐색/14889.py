from itertools import combinations
n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
team=[]
result=[]

def stat(x):
    star=0
    for i in combinations(x,2):
        a,b=i
        star+=arr[a-1][b-1]+arr[b-1][a-1]
    return star

for i in combinations(range(1,n+1),n//2):
    team.append(stat(list(i)))

for i in range(len(team)//2):
    result.append(abs(team[i]-team[len(team)-1-i]))
print(min(result))
    
