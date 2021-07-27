T=int(input())
for i in range(T):
    n=int(input()) 
    list_sosu=[]
    x=[False,False]+[True]*(n-1)
    for j in range(2,n+1):
        if x[j] and j>0:
            list_sosu.append(j)        
        for k in range(j*j,n+1,j):
            x[k]=False
    max1=0
    for l in list_sosu:
        cha=n-l
        for m in list_sosu:
            if cha==m:
                if max1<m*l:
                    max1=m*l              
                    a=l
                    b=m
    print(a,b)

    
   
    