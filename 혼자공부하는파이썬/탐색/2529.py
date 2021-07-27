from itertools import permutations
k=int(input())
arr=list(map(str,input().split()))
num=[i for i in range(10)]
result=[]

def sol(case):
    for i in range(len(arr)):
        if arr[i]==">" and case[i]<case[i+1]:
            return False
        elif arr[i]=="<" and case[i]>case[i+1]:
            return False
    return True
for i in permutations(num,k+1):
    if sol(i):
        result.append(i)
print(*result[-1],sep="")
print(*result[0],sep="")