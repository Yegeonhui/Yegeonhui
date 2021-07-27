def sol(num):
    for j in range(1,10**15):
        n=bin((num+j)^(num))
        a=0
        for i in range(2,len(n)):
            a+=int(n[i])
        if a<3:
            return num+j

def solution(numbers):
    answer=[]
    for i in numbers:
        answer.append(sol(i))
    return answer


print(solution([2,7]))