import sys
n,k=map(int,sys.stdin.readline().split())
num=list(map(str,sys.stdin.readline()))
stack=[]
copy_k=k
for i in range(n):
    while len(stack)>0 and copy_k>0:
        if stack[-1]<num[i]:
            stack.pop()
            copy_k-=1
        else:
            break
    stack.append(num[i])
    print(stack)
print(*stack[0:n-k],sep="")