n,k=map(int,input().split())
arr=[]
check=0
ysps=[i for i in range(1,n+1)]
while ysps:
    check+=k-1
    while check>= len(ysps):
        check-=len(ysps)
    arr.append(ysps.pop(check))
print("<"+', '.join(map(str,arr))+">")