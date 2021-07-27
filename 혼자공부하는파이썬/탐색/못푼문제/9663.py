n=int(input())
count=0
def sol(arr):
    global count
    if len(arr)==n:
        count += 1
    else:
        for i in range(n):
            if i in arr:
                continue
            for j in range(len(arr)):
                if abs(i - arr[j]) == len(arr) - j: 
                    break
            else: 
                arr.append(i)
                sol(arr)
                arr.pop()
    print(arr)

for i in range(n):
    sol([i])
print(count)