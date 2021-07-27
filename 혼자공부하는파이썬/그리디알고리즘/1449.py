n,l=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
tape=arr[0]
count=1
for i in range(1,n):
    if tape+l-0.5>=arr[i]+0.5:
        continue
    else:
        tape=arr[i]
        count+=1
print(count)

        