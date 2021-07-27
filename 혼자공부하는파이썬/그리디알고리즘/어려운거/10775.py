import sys
def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]
def union(x,y):
    x,y=find(x),find(y)
    parent[x]=y
g=int(sys.stdin.readline())
p=int(sys.stdin.readline())
parent=[i for i in range(g+1)]
ans=0
for i in range(p):
    v=int(sys.stdin.readline())
    v=find(v)
    if v!=0:
        union(v,v-1)
        print(v,parent)
        ans+=1
    else:
        break
print(ans)
