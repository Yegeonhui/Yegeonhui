X=int(input())
num=1
while True: 
    if num*(num+1)//2>=X:
        break
    else:
        num+=1

val=X-(num-1)*num//2
if num%2==0:
    print(str(val)+"/"+str(num-val+1))
else:
    print(str(num-val+1)+"/"+str(val))
