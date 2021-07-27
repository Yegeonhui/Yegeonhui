def two(n):
    answer=0
    while n!=0:
        n//=2
        answer+=n
    return answer
def five(n):
    answer=0
    while n!=0:
        n//=5
        answer+=n
    return answer
n,m=map(int,input().split())
if m==0:
    print(0)
else:
    print(min(two(n)-two(m)-two(n-m),five(n)-five(m)-five(n-m)))