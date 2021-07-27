n=int(input())
arr=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
max_num=-int(1e9)
min_num=int(1e9)
def sol(x,y):
    global arr,a,b,c,d,max_num,min_num,n
    if y==n:
        max_num=max(max_num,x)
        min_num=min(min_num,x)
    else:
        if a>0:
            a-=1
            sol(x+arr[y],y+1)
            a+=1
        if b>0:
            b-=1
            sol(x-arr[y],y+1)
            b+=1
        if c>0:
            c-=1
            sol(x*arr[y],y+1)
            c+=1
        if d>0:
            d-=1
            if x<0:    
                sol(-((-x)//arr[y]),y+1)
            else:
                sol(x//arr[y],y+1)
            d+=1
sol(arr[0],1)
print(max_num)
print(min_num)