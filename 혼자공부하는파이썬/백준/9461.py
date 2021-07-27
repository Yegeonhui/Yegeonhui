def fibo(x):
    num=[1]*106
    num[3]=2
    num[4]=2
    for i in range(5,x+5):
        num[i]=num[i-1]+num[i-5]
    return num[x]

t=int(input())
for i in range(t):
    print(fibo(int(input())-1))