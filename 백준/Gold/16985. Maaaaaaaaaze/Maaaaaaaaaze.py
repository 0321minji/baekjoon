import sys
from itertools import permutations, product
from collections import deque
input=sys.stdin.readline

layer=[]
for k in range(5):
    layer.append([list(map(int,input().split())) for _ in range(5)])

def rotate(pan):
    rotations=[pan]
    for _ in range(3):
        pan=[list(reversed(r)) for r in zip(*pan)]
        rotations.append(pan)
    return rotations

res=float('inf')
move=[[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
def bfs(maze):
    global res
    if maze[0][0][0]==0 or maze[4][4][4]==0:
        return
    visited=[[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0]=True
    
    que=deque()
    que.append((0,0,0,0))
    
    while que:
        x,y,z,dist=que.popleft()
        if dist>=res:
            #continue
            return
        if x==4 and y==4 and z==4:
            res=min(res,dist)
            return

        for dx,dy,dz in move:
            nx=x+dx; ny=y+dy; nz=z+dz 
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if not visited[nx][ny][nz] and maze[nx][ny][nz]==1:
                    visited[nx][ny][nz]=True
                    que.append((nx,ny,nz,dist+1))
        
            
rotation=[]
for l in layer:
    rotation.append(rotate(l))

for permutation in permutations(range(5)):
    for rote in product(range(4),repeat=5):
        maze=[]
        for idx,r_index in zip(permutation,rote):
            maze.append(rotation[idx][r_index])
        if maze[0][0][0] == 0 or maze[0][0][0]==4:
            continue
        bfs(maze)
        if res==12:
            print(res)
            exit()

print(res if res!=float('inf') else -1)
