import sys
from collections import deque
input=sys.stdin.readline


n=int(input())
k=int(input())
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1
    
l=int(input())
directs=deque(list(map(str,input().split())) for _ in range(l))
direct=0
move=[[0,1],[1,0],[0,-1],[-1,0]]
time=0
x=y=1
snake=deque([(1,1)])

while True:
    time+=1
    nx=x+move[direct][0]
    ny=y+move[direct][1]
    # print(snake,time)
    if not (0<nx<=n and 0<ny<=n) or (nx,ny) in snake:
        break
    snake.append((nx,ny))
    if graph[nx][ny]==1:
        graph[nx][ny]=0
    else:
        snake.popleft()
    if directs and directs[0][0]==str(time):
        _,nxt=directs.popleft()
        if nxt=='L':
            direct-=1
        else:
            direct+=1
        direct%=4
    x=nx; y=ny
print(time)    
            
        
    