import sys
from collections import deque
n=int(sys.stdin.readline())
deq=deque([])
for i in range(n):
    cmd=sys.stdin.readline().split()
    x=0
    if len(cmd)==2:
        x=int(cmd[1])
        cmd=cmd[0]
    else:
        cmd=cmd[0]
    if cmd=="push_front":
        deq.appendleft(x)
    elif cmd=="push_back":
        deq.append(x)
    elif cmd=="pop_front":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif cmd=="pop_back":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    elif cmd=="size":
        print(len(deq))
    elif cmd=="empty":
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif cmd=="front":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    elif cmd=="back":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])