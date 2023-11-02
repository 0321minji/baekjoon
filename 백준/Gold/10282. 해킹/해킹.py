import sys
input=sys.stdin.readline
import heapq

t=int(input())
INF=10**8
for _ in range(t):
    n,d,c=map(int,input().split())
    com=[[] for _ in range(n+1)]
    visit=[INF]*(n+1)
    #com 인접리스트
    for _ in range(d):
        a,b,s=map(int,input().split())
        com[b].append([a,s])

    pq=[]
    #탐색
    heapq.heappush(pq,[0,c])
    cnt=0
    time=0
    while pq:
        t,cn=heapq.heappop(pq)
        if visit[cn]<=t:
            continue
        visit[cn]=t
        cnt+=1
        time=t
        for nc,nt in com[cn]:
            if visit[nc]>nt+t:
                heapq.heappush(pq,[nt+t,nc])
    print(cnt,time)
