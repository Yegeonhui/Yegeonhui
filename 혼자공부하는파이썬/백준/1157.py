list1=list(map(input().lower().count,(map(chr,range(97,123)))))
max1=max(list1)
count=0
a=0
for i in range(97,123):
    if list1[i-97]==max1:
        a=i-97
        count+=1
if count>=2:
    print("?")
else:
    print(chr(97+a).upper())