n=int(input())
arr=list(map(int,input().split()))
result=[[] for _ in range(n)]
for i in range(n):
    if i==0:
        result[i].append(arr[i])
    else:
        for j in range(0,i):
            if result[j][-1]<arr[i]:
                if len(result[i])-1<len(result[j]):
                    result[i]=result[j]+[arr[i]]
        if not result[i]:
            result[i].append(arr[i])
        print(result)
      
dap=0
for i in range(n):
    dap=max(dap,len(result[i]))
print(dap)