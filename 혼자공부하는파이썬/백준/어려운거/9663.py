count=0
def solution(arr):
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
                solution(arr)
                arr.pop()

n=int(input())
for i in range(n):
    solution([i])
print(count)
