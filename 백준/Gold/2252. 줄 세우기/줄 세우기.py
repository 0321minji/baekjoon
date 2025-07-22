import sys
input=sys.stdin.readline

from collections import deque,defaultdict

n,m=map(int,input().split())
degrees=[0 for _ in range(n+1)]
graph=defaultdict(list)

for _ in range(m):
    a,b=map(int,input().split())
    degrees[b]+=1
    graph[a].append(b)
    
que=deque([])

for i in range(1,n+1):
    if degrees[i]==0:
        que.append(i)

for _ in range(n):
    if not que:
        break
    
    now=que.popleft()
    print(now)
    
    for i in graph[now]:
        degrees[i]-=1
        if degrees[i]==0:
            que.append(i)
