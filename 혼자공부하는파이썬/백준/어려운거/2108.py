from sys import stdin
import collections
n = int(stdin.readline())
x=[]
for i in range(n):
    x.append(int(input()))
x.sort()
c=collections.Counter(x)
frq_tuple=c.most_common(2)
print(round(sum(x)/n))
print(x[n//2])
if len(frq_tuple) <= 1 :
    print(frq_tuple[0][0])
else :
    if frq_tuple[0][1] == frq_tuple[1][1]:
        print(frq_tuple[1][0])
    else :
        print(frq_tuple[0][0])

print(max(x)-min(x))