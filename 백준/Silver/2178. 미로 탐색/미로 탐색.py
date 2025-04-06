import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
#붙어서 입출력
graph=[]

for _ in range(n):
    graph.append(list(input().rstrip()))
#print(graph)

move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve():
    que=deque([(0,0,1)])
    graph[0][0]=2
    
    while que:
        x,y,cnt=que.popleft()

        if x==n-1 and y==m-1:
            print(cnt)
            return
        for a,b in move:
            nx=x+a; ny=y+b
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='1':
                que.append([nx,ny,cnt+1])
                graph[nx][ny]=2

solve()