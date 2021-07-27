n=int(input())
list_sort=[]
for i in range(n):
    x,y=map(int,input().split())
    list_sort.append([y,x])
list_sort.sort()
for i in range(len(list_sort)):
    print(list_sort[i][1],list_sort[i][0])
