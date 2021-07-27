N=[]
for i in range(9):
    N.insert(i,int(input()))

print(max(N))
for i in range(9):

    if max(N)==N[i]:
        print(i+1)