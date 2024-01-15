#그래프 초기화
def fill(n,fares):
    graph=[[10**8]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i]=0
    for a,b,d in fares:
        graph[a][b]=d
        graph[b][a]=d
    return graph

##dp랑 비슷...???
def solution(n, s, a, b, fares):
    answer = 10**8
    graph=fill(n,fares)
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(1,n+1):
        answer=min(answer,graph[s][i]+graph[i][a]+graph[i][b])

    
    return answer