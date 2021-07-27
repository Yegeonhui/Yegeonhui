n,k=map(int,input().split())
mul=1
mul1=1
for i in range(1,k+1):
    mul*=i
    mul1=mul1*(n-i+1)
print(mul1//mul)
