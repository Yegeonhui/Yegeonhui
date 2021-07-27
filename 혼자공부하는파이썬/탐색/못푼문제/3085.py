n=int(input())
arr=[list(map(str,input())) for i in range(n)]
result=0

def width():
    global result
    for i in range(n):
        count=1
        for j in range(n-1):
            if arr[i][j]==arr[i][j+1]:
                count+=1
            else:
                if result<count:
                    result=count
                count=1
        if result<count:
            result=count

def height():
    global result
    for i in range(n):
        count=1
        for j in range(n-1):
            if arr[j][i]==arr[j+1][i]:
                count+=1
            else:
                if result<count:
                    result=count
                count=1
        if result<count:
            result=count

for i in range(n):
    for j in range(n-1):
        arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
        width()
        height()
        arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j]
for i in range(n):
    for j in range(n-1):
        arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
        width()
        height()
        arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
print(result)