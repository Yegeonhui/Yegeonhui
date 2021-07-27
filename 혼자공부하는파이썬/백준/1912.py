n=int(input())
seq=list(map(int,input().split()))
seq_list=[0 for _ in range(n)]
result=-1001
for i in range(n):
    seq_list[i]=max(seq_list[i-1]+seq[i],seq[i])
    result=max(result,seq_list[i])
print(result)