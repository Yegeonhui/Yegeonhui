
def plus_(N_1,N_2):
    
    X=str(int(N_1)+int(N_2))
    result=N_2+X[-1]
    return result

N=input()
B=N
if int(N)<10:
    B=N.zfill(2)

count=1
while True:
    A=plus_(B[0],B[-1])
    if int(N)==int(A):
        break
    else :
        count+=1
    B=A
print(count)
