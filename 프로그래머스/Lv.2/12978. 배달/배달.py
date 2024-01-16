import heapq
def solve(dist,graph):
    pq=[]
    heapq.heappush(pq,[1,0])
    
    while pq:
        node, wei = heapq.heappop(pq)
        for nxt, nxt_w in graph[node]:
            if wei+nxt_w < dist[nxt]:
                dist[nxt]=wei+nxt_w
                heapq.heappush(pq,[nxt,wei+nxt_w])
    

def solution(N, road, K):
    answer = 0
    dist=[10**8]*(N+1)
    dist[1]=0
    
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    solve(dist,graph)
    for i in dist:
        if i<=K:
            answer+=1
    return answer