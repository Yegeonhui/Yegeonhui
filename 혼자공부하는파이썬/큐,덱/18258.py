import sys
from collections import deque
n=int(sys.stdin.readline())
que=deque([])
num=0
for i in range(n):
    cmd=sys.stdin.readline().split()
    if len(cmd)==2:
        num=int(cmd[1])
        cmd=cmd[0]
    else:
        cmd=cmd[0]
    if cmd=="push":
        que.append(num)
    elif cmd=="pop":
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    elif cmd=="size":
        print(len(que))
    elif cmd=="empty":
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif cmd=="front":
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    elif cmd=="back":
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])    