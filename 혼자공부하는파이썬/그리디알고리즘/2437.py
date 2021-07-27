n=int(input())
arr=list(map(int,input().split()))
arr.sort()
hap=arr[0]+1
if arr[0]!=1:
    print(1)
else:
    for i in range(1,n):
        if hap<arr[i]:
            break
        else:    
            hap+=arr[i]
    print(hap)