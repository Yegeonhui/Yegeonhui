n=int(input())
tri=[]
tri_mid=[]
for i in range(n):
    tri.append(list(map(int,input().split())))
tri[1][0]+=tri[0][0]
tri[1][1]+=tri[0][0]
for i in range(2,n):
    tri[i][0]=tri[i][0]+tri[i-1][0]
    tri[i][-1]=tri[i][-1]+tri[i-1][-1]
    for j in range(1,i):
        tri[i][j]=tri[i][j]+max(tri[i-1][j-1],tri[i-1][j])
        tri_mid.append(tri[i][j])
print(max(tri[i][0],tri[i][-1],max(tri_mid)))
