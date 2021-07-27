n=str(input())
list_n=[]
for i in range(len(n)):
    list_n.append(n[i])
print(*list(reversed(sorted(list_n))),sep="")