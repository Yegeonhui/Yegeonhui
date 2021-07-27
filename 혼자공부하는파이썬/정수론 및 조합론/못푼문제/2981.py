def mul(a,b):
    if b==0:
        return a
    else:
        return mul(b,a%b)

n=int(input())
m=[0 for _ in range(n)]
m_cha=[0 for _ in range(n)]
for i in range(n):
    m[i]=int(input())
m.sort(reverse=True)

for i in range(n):
    m_cha[i]=(m[i-1]-m[i])

if len(m_cha)==1:
    answer=m_cha[0]
elif len(m_cha)==2:
    answer=mul(m_cha[0],m_cha[1])
else:
    answer=m_cha[0]
    for i in range(1,len(m_cha)):
        answer=mul(answer,m_cha[i])

answer_arr=[]
for i in range(2,answer+1):
    if answer%i==0:
        answer_arr.append(i)
print(*answer_arr)