while True:
    arr=input()
    if arr==".":
        break
    stack=[]
    for i in arr:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")" :
            if len(stack)==0:
                stack.append(i)
                break
            if stack[-1]=="(":
                stack.pop()
            else:
                break
        elif i=="]":
            if len(stack)==0:
                stack.append(i)
                break
            if stack[-1]=="[":
                stack.pop()
            else:
                break
    if len(stack)==0:
        print("yes")
    else:
        print("no")