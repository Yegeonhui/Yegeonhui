n=int(input())
result=1
for i in range(1,n+1):
    result*=i
result=str(result)
print(result)
arr=[0 for _ in range(len(result))]
for i in range(len(result)):
    arr[i]=result[i]
count=0
for i in reversed(arr):
    if i=="0":
        count+=1
    else:
        break
print(count)