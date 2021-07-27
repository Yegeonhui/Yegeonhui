N=int(input())
res=N
for i in range(N):
    string=input()
    char_list=[]
    pivot=string[0]
    for j in range(1,len(string)):
        if pivot != string[j]:
            if pivot not in char_list :
                char_list.append(pivot)
                pivot=string[j]

            if pivot in char_list:
                res-=1
                break

print(res)
    