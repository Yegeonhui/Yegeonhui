def solution(arr,x,y,empty):
    if x==m:
        print(*empty)
    else:
        for i in range(y,n+1):
            empty.append(i)
            solution(arr,x+1,i,empty)
            empty.pop()
        
n,m=map(int, input().split())
list_=[]
for i in range(1,n+1):
    list_.append(i)
solution(list_,0,1,[]) 