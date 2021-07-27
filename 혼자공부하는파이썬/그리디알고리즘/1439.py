s=list(map(str,input()))
tmp=s[0]
count=0
for i in range(1,len(s)):
    if tmp!=s[i]:
        tmp=s[i]
        count+=1
if count%2==1:
    result=count//2+1
else:
    result=count//2
print(result)