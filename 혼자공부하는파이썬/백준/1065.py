def han(n):
    count=0
    for i in range(1,n+1):
        if i<100:
            count+=1
        else:
            if int(str(i)[2])-int(str(i)[1])==int(str(i)[1])-int(str(i)[0]):
                count+=1
    return count

N=int(input())
print(han(N))


