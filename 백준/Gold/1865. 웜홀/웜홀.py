import sys, heapq
input=sys.stdin.readline

def solve():
    dist=[10**8]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            for e,wei in load[j]:
                if dist[e]>dist[j]+wei:
                    dist[e]=dist[j]+wei
                    if i==n:
                        return 'YES'
    return 'NO'


tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    load=[[] for _ in range(n+1)]
    for _ in range(m):
        s,e,t=map(int,input().split())
        load[s].append([e,t])
        load[e].append([s,t])
    for _ in range(w):
        s,e,t=map(int,input().split())
        load[s].append([e,-t])

    print(solve())
