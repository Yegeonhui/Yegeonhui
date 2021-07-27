n=int(input())
arr=list(map(int,input().split()))

result=(4*(arr[0]+arr[1])+(n-2)*4*arr[0])*n+arr[2]*4+arr[1]*(n-2)*4+arr[0]*(n-2)**2
print(result)