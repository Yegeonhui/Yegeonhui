T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    N_=N%H
    N_1=N//H+1
    if N_==0:
        N_=H
        N_1-=1
    if N_1<10:
        N_1=str(0)+str(N_1)
    print(str(N_)+str(N_1))
