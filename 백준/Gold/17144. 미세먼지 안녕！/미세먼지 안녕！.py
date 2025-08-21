import sys
input=sys.stdin.readline
from collections import defaultdict

r,c,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(r)]
move_up=[(-1,0),(0,1),(1,0),(0,-1)]
move_down=[(1,0),(0,1),(-1,0),(0,-1)]

for i in range(r):
    if board[i][0]==-1:
        air=i
        break
    
def air_move(x,y):
    cnt=0
    now=board[x][y]
    nxt=now//5
    for dx,dy in move_up:
        nx=x+dx; ny=y+dy
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny]!=-1:
                cnt+=1
                temp[(nx,ny)]+=(nxt)
    temp[(x,y)]+=(now-nxt*cnt)
    

def check(m,x,y):
    if m==move_up:
        return 0<=x<=air and 0<=y<c
    else:
        return air<x<r and 0<=y<c
def circular(x,y,m):
    index=0
    while index<4:
        dx,dy=m[index]
        while True:
            nx=x+dx; ny=y+dy
            if check(m,nx,ny):
                if board[nx][ny]>=0:
                    board[x][y]=board[nx][ny]
                    board[nx][ny]=0
                x,y=nx,ny
            else:
                index+=1
                break

def wind_move():
    board[air-1][0]=0
    circular(air-1,0,move_up)
    board[air+2][0]=0
    circular(air+2,0,move_down)
for _ in range(t):
    temp=defaultdict(int)
    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                air_move(i,j)
    
    for x,y in temp:            
        board[x][y]=temp[(x,y)]
    # print(board)
    wind_move()
    # print(board)

res=0
for r in board:
    res+=sum(r)
print(res+2)