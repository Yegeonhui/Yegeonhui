k=int(input())
arr=[]
for i in range(k):
    arr.append(int(input()))
    if arr[-1]==0:
        if len(arr)==1:
            arr[0]=0
        elif len(arr)==2:
            arr[0]=0
        else:
            arr.pop()
            arr.pop()
print(sum(arr))
                

    