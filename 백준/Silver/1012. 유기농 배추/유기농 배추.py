import sys
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve(x,y):
    que=[(x,y)]
    while que:
        x,y=que.pop()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]:
                graph[nx][ny]=0
                que.append((nx,ny))
                

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    #print(graph)
    result=0
    for _ in range(k):
        x,y=map(int,input().split())
        
        graph[y][x]=1
    for i in  range(n):
        for j in range(m):
            if graph[i][j]:
                graph[i][j]=0
                solve(i,j)
                result+=1
    print(result)
