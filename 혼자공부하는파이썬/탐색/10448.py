import sys
input=sys.stdin.readline
t=int(input())
num=[0]*1001
gauss=[n*(n+1)//2 for n in range(1,46)]
for i in gauss:
        for j in gauss:
            for k in gauss:
                if i+j+k<=1000:
                    num[i+j+k]=1 
for i in range(t):
    print(num[int(input())])