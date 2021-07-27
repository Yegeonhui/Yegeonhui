n=int(input())
x=[]
for i in range(n):
    x.append(int(input()))
for i in range(n):
    a=sorted(x)
    print(a[i])