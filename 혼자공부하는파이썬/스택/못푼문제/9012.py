t=int(input())
for i in range(t):
    arr=list(map(str,input()))
    stack=[]
    for j in range(len(arr)):
        if arr[j]=="(":
            stack.append("(")
        else:
            if len(stack)==0:
                stack.append(")")
                break
            else:    
                stack.pop()
    if len(stack)!=0:
        print("NO")
    else: 
        print("YES")

