import sys
input=sys.stdin.readline

t=int(input())
def solve(n):
    global check

    for i in range(1,n+1):
        for j in range(1,n+1):
            for e,wei in road[j]:
                if(dist[e]>wei+dist[j]):
                    dist[e]=wei+dist[j]
                    if(i==n):
                        check=1
    
for i in range(t):
    n,m,w=map(int,input().split())
    road=[[] for _ in range(n+1)]
    inf=10**9
    dist=[inf]*(n+1)


    for i in range(m):
        s,e,t=map(int,input().split())
        road[s].append((e,t)) #t 증가하는 시간
        road[e].append((s,t)) # 양방향 그래프라서
    for i in range(w):
        s,e,t=map(int,input().split())
        road[s].append((e,-t)) #이때 t 줄어드는 시간

    check=0

    solve(n)

    if check==1:
        print('YES')

    else:
        print('NO')
