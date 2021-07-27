def fibo(n):
    num=[0]*10001
    num[0]=0
    num[1]=1
    for i in range(2,n+1):
        num[i]=num[i-1]+num[i-2]
    return num[n]

n=int(input())
print(fibo(n))
