arr=str(input().split())
ucpc=["U","C","P","C"]
count=0
for i in arr:
    if i in ucpc[count]:
        count+=1
    if count==4:
        break
if count==4:
    print("I love UCPC")
else:
    print("I hate UCPC")