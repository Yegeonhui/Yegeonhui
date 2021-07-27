list_x=[]
list_y=[]
for i in range(3):
    x,y=map(int,input().split())
    list_x.append(x)
    list_y.append(y)
for i in list_x:
    if list_x.count(i)==1:
        a=i
for i in list_y:
    if list_y.count(i)==1:
        b=i
print(a,b)