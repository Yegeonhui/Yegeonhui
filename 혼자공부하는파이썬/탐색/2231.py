n=int(input())
for i in range(1,n+1):
    dap=i
    i=str(i)
    result=0
    for j in range(len(i),-1,-1):
        i=int(i)
        result+=i//10**j
        i=i-i//10**j*10**j
    if dap+result==n:
        print(dap)
        break
else:
    print(0)
            
            