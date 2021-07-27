def d(n):
    a=list(map(int,str(n)))
    result=sum(a)+n
    return result    

D=set([])
for i in range(1,10000):
    D.add(d(i))
D1=set(range(1,10001))
D2=sorted(list(D1-D))
for i in range(len(D2)):
    print(D2[i])