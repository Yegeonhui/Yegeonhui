a,b=input().split()
a1=""
b1=""
for i in reversed(range(len(a))):
    a1+=a[i]
    b1+=b[i]
    
if a1>b1:
    print(a1)
else:
    print(b1)


    #print(max(input()[::-1].split()))