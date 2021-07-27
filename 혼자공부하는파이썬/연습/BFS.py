from collections import deque
graph=[[],[2,3],[1,5,6],[1,4],[3],[2],[2]]
visited=[False]*7

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

bfs(graph,1,visited)