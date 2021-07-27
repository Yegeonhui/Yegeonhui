c=int(input())
count=0
for i in range(c):
    T=list(map(int,input().split()))
    avg=sum(T[1:len(T)])/(len(T)-1)
    count=0
    for j in range(1,len(T)):
       
        if avg<T[j]:
            count+=1
    print("%.3f%%"%(count/(len(T)-1)*100))

