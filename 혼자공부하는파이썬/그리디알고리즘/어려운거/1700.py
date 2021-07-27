n,k=map(int,input().split())
multi=[0 for i in range(n)]
plug=list(map(int,input().split()))
num=0
swap=0
max_l=0
result=0
for i in plug:
    if i in multi:
        pass
    elif 0 in multi:
        multi[multi.index(0)]=i
    else:
        for j in multi:
            if j not in plug[num:]:
                swap=j
                break
            elif plug[num:].index(j)>max_l:
                max_l=plug[num:].index(j)
                swap=j
        multi[multi.index(swap)]=i
        max_l=swap=0
        result+=1
    num+=1
print(result)
