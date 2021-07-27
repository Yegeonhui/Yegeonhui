import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    m=list(map(str,input().split()))
    if len(m)==2:
        cmd=m[0]
        num=int(m[1])
    else:
        cmd=m[0]
    if cmd=="push":
        stack.append(num)
    elif cmd=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd=="size":
        print(len(stack))
    elif cmd=="empty":
        if len(stack)==0:
            print(1)
        else: 
            print(0)
    elif cmd=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])