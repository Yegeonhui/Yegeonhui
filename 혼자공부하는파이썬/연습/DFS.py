graph=[[],[2,3],[1,5,6],[1,4],[3],[2],[2]]
visited=[False]*7

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)