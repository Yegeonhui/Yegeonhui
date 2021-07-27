def solution(words):
    words=list(set(words))
    words.sort()
    words.sort(key=lambda x:len(x))
    for word in words:
        print(word)

n=int(input())
words=[input() for _ in range(n)]
solution(words)