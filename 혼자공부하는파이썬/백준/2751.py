n=int(input())
x=[]
for i in range(n):
    x.append(int(input()))
a=list(set(sorted(x)))
for i in range(len(a)):
    print(a[i])
