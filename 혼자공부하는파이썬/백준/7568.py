n=int(input())
list_x=[]
list_y=[]
rank_list=[]

for i in range(n):
    x,y=list(map(int,input().split()))
    list_x.append(x)
    list_y.append(y)

for i in range(n):
    count=1
    for j in range(n):
        if int(list_x[i])<int(list_x[j]) and int(list_y[i])<int(list_y[j]):
            count+=1
    rank_list.append(count)
print(*rank_list)