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

arr_rev=list(reversed(arr))
result_rev=[[] for i in range(n)]
for i in range(n):
    if i==0:
        result_rev[i].append(arr_rev[i])
    else:
        for j in range(0,i):
            if result_rev[j][-1]<arr_rev[i]:
                if len(result_rev[i])-1<len(result_rev[j]):
                    result_rev[i]=result_rev[j]+[arr_rev[i]]
        if not result_rev[i]:
            result_rev[i].append(arr_rev[i])
print(result_rev)

dap=0
for i in range(n):
    dap=max(dap,len(result[i])+len(result_rev[-i-1]))
print(dap-1)