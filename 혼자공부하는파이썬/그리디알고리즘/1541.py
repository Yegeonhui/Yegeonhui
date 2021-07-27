way=list(map(str,input().split('-')))
result=0
for i in range(len(way)):
    if i==0:
        for j in way[i].split("+"):
            result+=int(j)
    else:
        for j in way[i].split("+"):
            result-=int(j)

print(result)