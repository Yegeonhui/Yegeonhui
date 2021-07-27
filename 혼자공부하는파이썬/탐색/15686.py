from itertools import combinations
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
chicken=[]
house=[]
result_arr=[]

def sol(arr,house):
    result=0
    for a,b in house:
        dis=1e9
        for c,d in arr:
            dis=min(dis,abs(a-c)+abs(b-d))
        result+=dis
    return result

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append([i,j])
        if arr[i][j]==1:
            house.append([i,j])

for i in combinations(chicken,m):
    result_arr.append(sol(list(i),house))
print(min(result_arr))
