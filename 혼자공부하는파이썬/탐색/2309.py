arr=[]
for i in range(9):
    arr.append(int(input()))
arr.sort()
result=sum(arr)-100
for i in range(9):
    for j in range(1,9):
        if len(arr)==7:
            break
        else:
            if arr[i]+arr[j]==result:
                arr.pop(j)
                arr.pop(i)
                break
for i in range(7):
    print(arr[i])