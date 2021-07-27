def sum1(N):
    result=0
    for i in range(len(N)):
        result+=a[i]
    return result

a=list(map(int,input().split()))
print(sum1(a))