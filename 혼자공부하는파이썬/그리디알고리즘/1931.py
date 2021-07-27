n=int(input())
conf=[]
for i in range(n):
    conf.append(list(map(int,input().split())))
conf.sort(key=lambda x:(x[1],x[0]))
answer=1
count=0
for i in conf:
    if count==0:
        endtime=i[1]
        count+=1
    elif endtime<=i[0]:
        endtime=i[1]
        answer+=1
print(answer)
