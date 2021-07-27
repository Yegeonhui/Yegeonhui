N=int(input())
if N==1:
    print(1)
list_=[2]
for i in range(1,N):
    list_.append(list_[i-1]+6*i)
    if list_[i]>N:
        print(i+1)
        break
