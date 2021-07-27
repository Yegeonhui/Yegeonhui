n=int(input())
m=int(input())
arr=list(map(str,input().split()))

def search(n,arr):
    result=abs(n-100)
    for i in range(1000001):
        is_possible=True
        for j in str(i):
            if j in arr:
                is_possible=False
                break
        if is_possible:
            result=min(result,abs(n-i)+len(str(i)))
    return result

print(search(n,arr))


