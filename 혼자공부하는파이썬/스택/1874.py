n=int(input())
arr=[]
stack=[]
result=[]
cnt=1
for i in range(n):
    arr.append(int(input()))
for i in arr:
    while cnt<=i:
        stack.append(cnt)
        result.append("+")
        cnt+=1
    if stack.pop() !=i:
        result.append("NO")
    else:
        result.append("-")

if "NO" in result:
    print("NO")
else:
    for i in result:
        print(i)    