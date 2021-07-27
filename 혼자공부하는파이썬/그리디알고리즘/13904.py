n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
arr.sort(key=lambda arr:arr[1])
day=[0 for i in range(1001)]
for i in range(n-1,-1,-1):
    if day[arr[i][0]]==0:
        day[arr[i][0]]=arr[i][1]
    else:
        k=1
        while k!=arr[i][0]:
            if day[arr[i][0]-k]==0:
                day[arr[i][0]-k]=arr[i][1]
                break
            else:
                k+=1
print(sum(day))


    