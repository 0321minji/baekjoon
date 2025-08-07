#최장 거리 
import sys
from collections import defaultdict,deque
input=sys.stdin.readline
n=int(input())
graph=defaultdict(list)

for _ in range(n-1):
    s,e,d=map(int,input().split())
    graph[s].append([e,d])
    graph[e].append([s,d])
    
res=0
visited=[0]*(n+1)
que=deque([(1,0)])

res=0
while que:
    now,dist=que.popleft()
    res=max(res,dist)
    for nxt,cost in graph[now]:
        if not visited[nxt]:
            visited[nxt]=1
            que.append((nxt,dist+cost))


print(res)