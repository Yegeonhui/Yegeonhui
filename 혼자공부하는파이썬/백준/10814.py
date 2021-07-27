n=int(input())
member=[]
for i in range(n):
    member.append(list(map(str,input().split())))

member.sort(key=lambda x:int(x[0]))

for i in member:
    print(i[0],i[1])