S=str(input())
list1=[-1]*26
for i in reversed(range(len(S))):
    for j in range(97,123):
        if S[i]==chr(j):
            list1[j-97]=i

print(*list1)
        