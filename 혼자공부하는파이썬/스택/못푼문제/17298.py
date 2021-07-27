import sys
input=sys.stdin.readline
n=int(input())
m=list(map(int,input().split()))
nge=[-1 for _ in range(n)]
stack=[]
for i in range(len(m)):
    try:
        while m[stack[-1]]<m[i]:
            nge[stack.pop()]=m[i]
    except:
        pass
    stack.append(i)
for i  in range(n):
    print(nge[i],sep=' ')

