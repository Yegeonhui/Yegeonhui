croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
s_copy=s
ind=0

while True:
    for i in croatia: 
        if i in s:
            ind=s_copy.index(i)
            s_copy=s_copy[:ind]+'/'+s_copy[ind+len(i):]
            break
    if s_copy!=s:
        s=s_copy 
    else:
        break
    

print(len(s))

        