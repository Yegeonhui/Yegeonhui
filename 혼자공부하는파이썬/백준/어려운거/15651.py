def solution(arr,x,empty):
    if x==m:
        print(*empty)
    else:
        for i in range(n):
            empty.append(arr[i])
            solution(arr,x+1,empty)
            empty.pop()
    
n,m= map(int, input().split())
list_=[]
for i in range(1,n+1):
    list_.append(i)
solution(list_,0,[])