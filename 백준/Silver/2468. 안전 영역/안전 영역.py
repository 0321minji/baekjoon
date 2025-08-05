import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
MAX=max(map(max,graph))

cnt=0
move=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(a,b,visited):
    que=deque([(a,b)])
    
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if (0<=nx<n and 0<=ny<n) and not visited[nx][ny] and graph[nx][ny]>h:
                que.append((nx,ny))
                visited[nx][ny]=1
    
for h in range(MAX):
    temp=0
    visited=[[0 for _ in range(n)] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if graph[a][b]>h and not visited[a][b]:
                visited[a][b]=1
                bfs(a,b,visited)
                temp+=1
    cnt=max(temp,cnt)
print(cnt)    
                
