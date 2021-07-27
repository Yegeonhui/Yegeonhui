n=int(input())
tel=[[] for _ in range(n)]
for i in range(n):
    tel[i]=list(map(int,input().split()))
tel.sort()
stack=[[] for _ in range(n)]
for i in range(n):
    if i==0:
        stack[i].append(tel[i][1])
    else:
        for j in range(0,i):
            if stack[j][-1]<tel[i][1]:
                if len(stack[i])-1<len(stack[j]):
                    stack[i]=stack[j]+[tel[i][1]]
        if not stack[i]:
            stack[i].append(tel[i][1])
    
dap=0
for i in range(n):
    dap=max(dap,len(stack[i]))
print(n-dap)
