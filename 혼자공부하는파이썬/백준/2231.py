n=str(input())
for i in range(int(n)):
    a=0
    i_str=str(i)
    b=i
    for j in range(len(i_str)):
        a+=int(i_str[j])
      
    if a+b==int(n):
        print(i)
        break    
else:
    print(0)
