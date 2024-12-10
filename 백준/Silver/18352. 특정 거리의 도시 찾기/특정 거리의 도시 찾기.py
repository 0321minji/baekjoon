#18352
#bfs이용 가능 값이 모두 1이라서!

import sys
input=sys.stdin.readline

from collections import deque

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]

dis=[-1]*(n+1)
dis[x]=0 #시작위치

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

que=deque([x])

while(que):
    i=que.popleft()
    for nx in graph[i]:
        if dis[nx]==-1:
            dis[nx]=dis[i]+1
            que.append(nx)

for i in range(n+1):
    if dis[i]==k:
        print(i)
if k not in dis:
    print(-1)