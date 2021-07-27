def fibo(n):
    num0=[int(0)]*41
    num1=[int(0)]*41
    num0[0]=1
    num1[0]=0
    for i in range(1,n+1):
        num0[i]=num1[i-1]
        num1[i]=num1[i-1]+num0[i-1]
    return num0[n],num1[n]
t=int(input())
for _ in range(t):
    print(*fibo(int(input())))



