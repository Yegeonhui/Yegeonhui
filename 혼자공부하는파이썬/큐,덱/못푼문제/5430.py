t=int(input())
for i in range(t):
    p=list(input())
    n=int(input())
    arr=eval(input())
    error=False
    R_count=0
    D_count=0
    for i in p:
        if i=="R":
            R_count+=1
        else:
            try: 
                if R_count%2==0:
                    D_count+=1
                else:
                    arr.pop()
            except:
                error=True
                break
    if error or D_count>len(arr):
        print("error")
        continue
    if R_count%2==0:
        answer=arr[D_count:]
    else:
        answer=list(reversed(arr[D_count:]))
    print("[",end="")
    for i in range(len(answer)):
        if i==len(answer)-1:
            print(answer[i],end="")
        else:
            print("%s,"%(answer[i]),end="")
    print("]")