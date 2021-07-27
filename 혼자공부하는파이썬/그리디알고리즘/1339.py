n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=list(map(str,input()))
a=[0 for i in range(26)]
for i in arr:
    leng=len(i)
    for j in range(leng):
        a[ord(i[j])-65]+=10**(leng-j-1)
a.sort(reverse=True)
print(a)
result,count=0,9
for i in a:
    result+=count*i
    count-=1
print(result)
