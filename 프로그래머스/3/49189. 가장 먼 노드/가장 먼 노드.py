from collections import deque

def solution(n,edge):
    graph=[[] for _ in range(n+1)]
    dist=[-1]*(n+1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs():
        q=deque([1])
        dist[1]=0
        
        while q:
            temp=q.popleft()
            for i in graph[temp]:
                if dist[i]==-1:
                    q.append(i)
                    dist[i]=dist[temp]+1
    bfs()
    return dist.count(max(dist))