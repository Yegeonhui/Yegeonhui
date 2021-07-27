from itertools import permutations
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
array=[]
result_arr=[]
for i in permutations(arr,n):
    array=list(i)
    result=0
    for j in range(n-1):
        result+=abs(array[j]-array[j+1])
    result_arr.append(result)
print(max(result_arr))