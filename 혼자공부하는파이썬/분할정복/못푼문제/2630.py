n=int(input())
arr=[[] for i in range(n)]
blue=0
white=0
for i in range(n):
    arr[i]=list(map(int,input().split()))

def quad_tree(x,y,n):
    global arr,blue,white
    color=arr[y][x]
    double_break=False
    for i in range(x,x+n):
        if double_break:
            break
        for j in range(y,y+n):
            if arr[j][i]!=color:
                print(j,i,n)
                quad_tree(x,y,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                double_break=True
                break
    if not double_break:
        if arr[y][x]==1:
            blue+=1
        else:
            white+=1

quad_tree(0,0,n)
print(white)
print(blue)