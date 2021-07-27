dials_num = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
dials = input()
dials = dials.upper()
dials_sum = 0
for dial in dials:
    dials_sum += dials_num[ord(dial)-ord('A')]
print(dials_sum)

#print(sum(5*min(ord(x),88)//16-17for x in input()))