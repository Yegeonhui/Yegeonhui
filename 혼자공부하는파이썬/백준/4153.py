while True:
    list_a=list(map(int,input().split()))
    if list_a==[0,0,0]:
        break

    a=min(list_a)
    c=max(list_a)
    for i in list_a:
        if i!=a and i!=c:
            b=i
    if a**2+b**2==c**2:
        print("right")
    else:
        print("wrong")