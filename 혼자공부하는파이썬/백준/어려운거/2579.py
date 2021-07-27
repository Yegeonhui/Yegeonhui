n=int(input())
stairs=[0]*301
for i in range(1,n+1):
    stairs[i]=int(input())
score=[0]*301
score[1]=stairs[1]
score[2]=stairs[1]+stairs[2]
score[3]=max(stairs[3]+stairs[1],stairs[3]+stairs[2])
if n>=4:
    for i in range(4,len(stairs)):
        score[i]=max(stairs[i]+score[i-2],stairs[i]+stairs[i-1]+score[i-3])
print(score[n])

