n=int(input())
su=list(map(int,input().split()))
a,b,c,d=map(int,input().split())
max_num=-int(1e9)
min_num=int(1e9)
def solution(num,next_num):
    global su,a,b,c,d,max_num,min_num,n
    if next_num==n:
        max_num=max(max_num,num)
        min_num=min(min_num,num)
    else:
        if a>0:
            a-=1
            solution(num+su[next_num],next_num+1)
            a+=1
        if b>0:
            b-=1
            solution(num-su[next_num],next_num+1)
            b+=1
        if c>0:
            c-=1
            solution(num*su[next_num],next_num+1)
            c+=1
        if d>0:
            d-=1
            if num<0:    
                solution(-((-num)//su[next_num]),next_num+1)
            else:
                solution(num//su[next_num],next_num+1)
            d+=1
            
solution(su[0],1)
print(max_num)
print(min_num)
