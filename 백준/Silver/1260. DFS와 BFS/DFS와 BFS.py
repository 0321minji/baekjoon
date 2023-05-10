from collections import deque
import sys

input=sys.stdin.readline

n,m,v=map(int,input().split())
link=[[0]*(n+1) for _ in range(n+1)] #간선 행렬로 표현
visit=[0]*(n+1)
#default값은 0; 연결되거나 지나갔을경우 1


for i in range(m):
    x,y=map(int,input().split())
    link[x][y]=link[y][x]=1

def dfs(v):
    visit[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if(visit[i]==0 and link[v][i]==1): #방문안했고, 연결되있을 시
            dfs(i)

def bfs(v):
    visit[v]=0 #dfs실행 이후 default가 1이 됨->방문하면 0으로
    q=[v]

    while q:
        v=q.pop(0)
        print(v,end=' ')
        for i in range(1,n+1):
            if(visit[i]==1 and link[v][i]==1):
                q.append(i)
                visit[i]=0

dfs(v)
print()
bfs(v)