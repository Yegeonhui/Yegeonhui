n=int(input())
arr=[[] for i in range(n)]
for i in range(n):
    arr[i]=list(map(int,input()))
answer=""
def quad_tree(x,y,n):
    global answer
    img=arr[y][x]
    flag=False
    for i in range(x,x+n):
        if flag:
            break
        for j in range(y,y+n):
            if arr[j][i]!=img:
                answer+="("
                quad_tree(x,y,n//2)
                quad_tree(x+n//2,y,n//2)
                quad_tree(x,y+n//2,n//2)
                quad_tree(x+n//2,y+n//2,n//2)
                answer+=")"
                flag=True
                break
    if not flag:
        if arr[y][x] == 1: 
            answer+='1'
        else:
            answer+='0'
quad_tree(0,0,n)
print(answer)
