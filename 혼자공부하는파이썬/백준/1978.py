N=int(input())
list1=list(map(int,input().split()))

sosu=0
for i in list1:
    count=0
    for j in range(2,i+1):
        if i%j==0:
            count+=1
    if count==1:
        sosu+=1
        
print(sosu)
        


                 
