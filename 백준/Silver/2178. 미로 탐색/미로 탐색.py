import sys
input=sys.stdin.readline

def bfs():
    q=[(0,0,1)]
    while q:
        x,y,res=q.pop(0)
        for (dx,dy) in move:
            nx=x+dx
            ny=y+dy
            if nx==n-1 and ny==m-1:
                print(res+1)
                return
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]=='1':
                    q.append((nx,ny,res+1))
                    graph[nx][ny]=2

n,m=map(int,input().split())
graph=[]
move=[[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(n):
    graph.append(list(input().rstrip()))

graph[0][0]=2
bfs()