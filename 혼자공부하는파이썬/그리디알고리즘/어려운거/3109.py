r,c=map(int,input().split())
pipe=[[0] for i in range(r)]
for i in range(r):
    pipe[i]=list(map(str,input()))
dy=[-1,0,1]
dx=[1,1,1]
count=0

def sol(y,x):
	global count,state
	if y==-1 or y==r:
		return 
	if pipe[y][x]=="x":
		return 
	pipe[y][x]="x"
	if x==c-1:
		state=True
		count+=1
		return 
	for i in range(3):
		ny=y+dy[i]
		nx=x+dx[i]
		sol(ny,nx)
		if state:
			return
	
for i in range(r):
	state=False
	sol(i,0)
print(count)
