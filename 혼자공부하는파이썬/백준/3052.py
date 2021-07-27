N=[]
A=[]
count=0

count=0
for i in range(10):
    N.insert(i,int(input())%42)

A=N
for i in range(9):
    for j in range(i+1,10):
        if N[i]==N[j]:
            A[i]=-1

for i in range(10):
    if A[i]>=0:
        count+=1
print(count)


