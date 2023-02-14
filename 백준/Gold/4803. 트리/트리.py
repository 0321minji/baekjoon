import sys
from collections import deque

input=sys.stdin.readline

def dfs(prev,node,g,visited):
    #방문 체크
    visited[node]=True
    for nn in graph[node]:
        if nn==prev:
            continue
        if visited[nn]:
            return False
        if not dfs(node,nn,graph,visited):
            return False
    return True


i=1
n,m=map(int,input().split())
while n+m!=0:
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    t=0
    for v in range(1,n+1):
        if not visited[v]:
            if dfs(0,v,graph,visited):
                t+=1
    if t==0:
        print("Case "+str(i)+": No trees.")
    elif t==1:
        print("Case "+str(i)+": There is one tree.")
    else:
        print("Case "+str(i)+": A forest of "+str(t)+" trees.")

    n,m=map(int,input().split())
    i+=1
