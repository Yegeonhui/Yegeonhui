n=int(input())
def fibo(x):
    hap=0
    if x==0:
        return 0
    elif x==1:
        return 1
    elif x==2:
        return 1
    else:
        hap=fibo(x-2)+fibo(x-1)
    return hap

print(fibo(n))
