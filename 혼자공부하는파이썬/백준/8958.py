
N=int(input())



for j in range(N):
    T=list(map(str,input()))
    su=0
    count=1
    for i in range(len(T)):
    
        if T[i]=="O":
            su+=count 
            count+=1
        else :
            count=1 
    print(su)
    
