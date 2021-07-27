N=[]


for i in range(10):
    N.insert(i,int(input())%42)

print(len(set(N)))