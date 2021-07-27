m=1
n=1
while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    elif n%m==0:
        print("factor")
    elif m%n==0:
        print("multiple")
    elif n%m!=0 and m%n!=0:
        print("neither")
    