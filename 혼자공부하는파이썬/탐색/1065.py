n=int(input())
result=0
cha=[]
for i in range(1,n+1):
    if i<100:
        result+=1
    else:
        i=str(i)
        cha=int(i[0])-int(i[1])
        count=0
        for j in range(len(i)-1):
            if cha==int(i[j])-int(i[j+1]):
                count+=1
            if count==len(i)-1:
                result+=1
print(result)