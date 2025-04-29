import sys
input=sys.stdin.readline
from collections import defaultdict,deque

def bfs():
    que=deque([(0,0,0)])
    
    while que:
        x,y,res = que.popleft()
        if y==t:
            return res
        
        for i in [(x-2),(x-1),(x),(x+1),(x+2)]:
            for j in graph[i]:
                if abs(j-y)<=2 and j not in visited[i]:
                    visited[i].append(j)
                    que.append((i,j,res+1))

n,t=map(int,input().split())
graph=defaultdict(list)
visited=defaultdict(list)
for _ in range(n):
    x,y=map(int,input().split())
    graph[x].append(y)
graph[0].append(0)

res=bfs()
print(res if res else -1)