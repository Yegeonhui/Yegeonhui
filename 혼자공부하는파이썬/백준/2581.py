M=int(input())
N=int(input())

sosu=[]
for i in range(M,N+1):
    count=0
    for j in range(2,i+1):
        if i%j==0:
            count+=1
    if count==1:
        sosu.append(i)
if sosu==[]:
    print(-1)    
else:    
    print(sum(sosu))
    print(min(sosu))
