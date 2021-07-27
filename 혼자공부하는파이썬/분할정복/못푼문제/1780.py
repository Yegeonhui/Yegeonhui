n=int(input())
arr=[[] for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input().split()))
count_m=0
count_z=0
count_o=0
def tree(x,y,n):
    global count_m,count_z,count_o,arr
    flag=False
    num=arr[y][x]
    for i in range(x,x+n):
        if flag:
            break
        for j in range(y,y+n):
            if num!=arr[j][i]:
                tree(x,y,n//3)
                tree(x,y+n//3,n//3)
                tree(x,y+n//3*2,n//3)
                tree(x+n//3,y,n//3)
                tree(x+n//3,y+n//3,n//3)
                tree(x+n//3,y+n//3*2,n//3)
                tree(x+n//3*2,y,n//3)
                tree(x+n//3*2,y+n//3,n//3)
                tree(x+n//3*2,y+n//3*2,n//3)
                flag=True
                break
    if not flag:
        if arr[y][x]==-1:
            count_m+=1
        elif arr[y][x]==0:
            count_z+=1
        else:
            count_o+=1
                
tree(0,0,n)
print(count_m)
print(count_z)
print(count_o)