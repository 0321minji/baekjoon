import sys
input = sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]
def dfs(a,b):
    que=[(a,b)]
    while que:
        a,b=que.pop()
        for dx,dy in move:
            nx=a+dx; ny=b+dy
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==1:
                que.append((nx,ny))
                graph[nx][ny]=2

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*(n) for _ in range(m)]
    result=0
    
    for _ in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                graph[i][j]=2
                result+=1
                dfs(i,j)
                #graph[i][j]=1
    print(result)
        
