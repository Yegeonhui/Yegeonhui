N,X=map(int,input().split())
list_1=input().split()
list_=[]
for i in range(0,N):
    if int(list_1[i])<X:
        list_.append(list_1[i])

print(list_)