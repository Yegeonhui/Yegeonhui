def fibo(x):
    num=[0]*(x+2)
    num[0]=1
    num[1]=2
    for i in range(2,n+1):
        num[i]=num[i-1]%15746+num[i-2]%15746
    return num[x]
n=int(input())
print(fibo(n-1)%15746)