import sys
input=sys.stdin.readline

n,m,x,y,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
requests=list(map(int,input().split()))
dice = [0]*6
# top_index=1
# right_index=3
top=1

move = {1:(0,1),
        2:(0,-1),
        3:(-1,0),
        4:(1,0)}

def roll(request):
    up,down,north,south,west,east=dice
    if request==1:
        dice[0],dice[1],dice[4],dice[5] = west,east,down,up
    elif request==2:
        dice[0],dice[1],dice[4],dice[5] = east,west,up,down
    elif request==3:
        dice[0],dice[1], dice[2],dice[3] = south,north,up,down
    else:
        dice[0],dice[1], dice[2],dice[3] = north,south,down,up
    
def solve(request):
    global x,y
    dx,dy=move[request]
    nx=x+dx; ny=y+dy;   
    if not (0<=nx<n and 0<=ny<m):
        return
    roll(request)
    # print(request,top,nxt,nx,ny)

    if board[nx][ny]==0:
        board[nx][ny]=dice[1]
    else:
        dice[1]=board[nx][ny]
        board[nx][ny]=0
    x,y=nx,ny
    # print(dice,top,dice[0])
    print(dice[0])

for request in requests:
    solve(request)