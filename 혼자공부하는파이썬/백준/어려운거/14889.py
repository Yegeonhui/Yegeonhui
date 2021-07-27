from itertools import combinations

def solution(arr):                                                         
    stat=0                                  
    for i in arr:
        for j in arr:
            stat+=list_[i][j]
    return stat

n=int(input())
team=[]
cha_list=[]
list_=[list(map(int,input().split())) for _ in range(n)]
for i in combinations(range(n),n//2):                                  
    team.append(i)                                      
for i in range(len(team)):
    cha_list.append(abs(solution(team[i])-solution(team[-i-1])))   
print(min(cha_list))
            
