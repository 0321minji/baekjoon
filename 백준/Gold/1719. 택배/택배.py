import sys , heapq
input=sys.stdin.readline

def solve(start,n):
    global graph, hub
    
    hq=[]
    for i in range(1,n+1):
        if i==start:
            continue
        heapq.heappush(hq,(graph[start][i],i))

    while hq:
        dist,node=heapq.heappop(hq)
        if graph[start][node]<dist:
            continue
        for nei in range(1,n+1):
            #자기 자신 pass
            if node==nei or start==nei:
                continue
            #node를 거치는 것이 start-nei 바로 가는 것보다  작다면 갱신
            if dist+graph[node][nei] < graph[start][nei]:
                graph[start][nei]=dist+graph[node][nei]
                heapq.heappush(hq,(graph[start][nei],nei))
                #***** 집하장도 갱신!!! ******* 
                hub[start][nei]=hub[start][node]
                


n,m=map(int,input().split())
#최단거리 값이랑 그때의 집하장 번호를 저장하는 리스트 따로따로
graph=[[10**8]*(n+1) for _ in range(n+1)]
hub=[['-']*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a][b]=graph[b][a]=t
    hub[a][b]=b
    hub[b][a]=a

for i in range(1,n+1):
    #i 정점으로부터 각 정점까지의 최단거리 구함
    solve(i,n)

for i in range(1,n+1):
    print(*hub[i][1:])
