import sys
input=sys.stdin.readline
from collections import deque

def dfs(now):
    visit[now]=1
    print(now,end=' ')
    for nxt in graph[now]:
        if not visit[nxt]:
            dfs(nxt)
          
def bfs():
    que=deque([v])
    visit[v]=1
    while que:
        now = que.popleft()
        print(now,end=' ')
        for nxt in graph[now]:
            if not visit[nxt]:
                visit[nxt]=1
                que.append(nxt)

n,m,v=map(int,input().split())
graph=[ [] for _ in range(n+1)]
edges = [list(map(int,input().split())) for _ in range(m)]
# edges.sort()

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visit=[0]*(n+1)
dfs(v)
print()
visit=[0]*(n+1)
bfs()