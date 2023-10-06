#1012
#상하좌우가 인접
import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    queue=[[x,y]]
    while queue:
        a,b=queue[0][0],queue[0][1]
        del queue[0]
        for i in range(4):
            q=a+dx[i]
            w=b+dy[i]
            if 0<=q<n and 0<=w<m and Map[q][w]==1:
                Map[q][w]=0
                queue.append([q,w])
    

t=int(input())
for i in range(t):
    count=0
    m,n,k=map(int,input().split())
    Map=[[0]*m for i in range(n)]   
    for i in range(k):
        y,x=map(int,input().split())
        Map[x][y]=1
    for a in range(n):
        for b in range(m):
            if Map[a][b]==1:
                bfs(a,b)
                Map[a][b]=0
                count+=1
    print(count)
