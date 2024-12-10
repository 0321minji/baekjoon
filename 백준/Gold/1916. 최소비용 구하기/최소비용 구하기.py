import sys
import heapq

input=sys.stdin.readline

n=int(input())
m=int(input())
inf=10**8

link=[[]for _ in range(n+1)]
dp=[inf]*(n+1)

def 다익스트라(start):
    dp[start]=0
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        wei,num=heapq.heappop(heap)
        if dp[num]<wei:
            continue
        for nxt, ww in link[num]:
            nxtw=wei+ww
            if dp[nxt]>nxtw:
                dp[nxt]=nxtw
                heapq.heappush(heap,(nxtw,nxt))

for i in range(m):
    a,b,w=map(int,input().split())
    link[a].append((b,w))

start,end=map(int,input().split())

다익스트라(start)
print(dp[end])
