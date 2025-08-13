import sys
from collections import deque
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
cnt=0

def bfs(x,y):
 
    que=deque([(x,y)])
    
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<h and 0<=ny<w and board[nx][ny]==1:
                board[nx][ny]=2           
                que.append((nx,ny))
    
while True:
    cnt=0
    w,h=map(int,input().split())
    if w==h==0:
        break
    board=[list(map(int,input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j]==1:
                board[i][j]=2
                bfs(i,j)
                cnt+=1
    print(cnt)
            
    