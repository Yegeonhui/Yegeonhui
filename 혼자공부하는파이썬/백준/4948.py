while True:
    n=int(input())
    if n==0:
        break

    x=[False,False]+[True]*(2*n-1)
    count=0
    for i in range(2,2*n+1):
        if x[i] and i>n:
            count+=1
        for j in range(i*i,2*n+1,i):
            x[j]=False
    print(count)
    