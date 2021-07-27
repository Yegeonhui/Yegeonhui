import sys 
i=int(sys.stdin.readline())
num=[0]*10001
for a in range(i):
    num[int(sys.stdin.readline())]+=1
for j in range(10001):
    if(num[j]>0):
        for f in range(num[j]):
            print(j)