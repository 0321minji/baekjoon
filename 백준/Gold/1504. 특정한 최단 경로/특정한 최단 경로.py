import sys, heapq
input=sys.stdin.readline

def get(start):
    #start 정점으로부터의 길이
    dist=[10**8]*(n+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        w, e = heapq.heappop(pq)
        for nxt,nxt_w in graph[e]:
            wei=nxt_w+w
            if dist[nxt]>wei:
                dist[nxt]=wei
                heapq.heappush(pq,(wei,nxt))
    return dist
    

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2=map(int,input().split())

v1d=get(v1)
v2d=get(v2)

#1->v1->v2->n or 1->v2->v1->n
result=min(v1d[1]+v1d[v2]+v2d[n], v2d[1]+v2d[v1]+v1d[n])

print(result if result<10**8 else -1)

