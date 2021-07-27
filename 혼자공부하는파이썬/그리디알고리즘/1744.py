n=int(input())
arr_p=[]
arr=[]
arr_m=[]
result=0
for i in range(n):
    temp=int(input())
    if temp>0:
        if temp==1:
            arr.append(temp)
        else:
            arr_p.append(temp)
    else:
        arr_m.append(temp)
arr_p.sort(reverse=True)
arr_m.sort()

def sol(x):
    result=0
    if len(x)%2==1:
        for i in range(0,len(x)-1,2):
            result+=x[i]*x[i+1]
        result+=x[-1]
    else:
        for i in range(0,len(x),2):
            result+=x[i]*x[i+1]
    return result

result=sol(arr_p)+sol(arr_m)+len(arr)
print(result)
