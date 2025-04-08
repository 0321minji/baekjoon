import sys
input=sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]
ground=[[5]*(n) for _ in range(n)]
tree=[[deque() for _ in range(n)]  for _ in range(n)]

for _ in range(m):
    x,y,z=map(int,input().split())
    tree[x-1][y-1].append(z)


def ss():
    for i in range(n):
        for j in range(n):
            dead=0
            alive=deque()
            for t in tree[i][j]:
                #양분
                if ground[i][j]>=t:
                    ground[i][j]-=t
                    alive.append(t+1)
                else: 
                    dead+=t//2
            tree[i][j]=alive
            ground[i][j]+=dead

def fw():
    move = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                #번식
                if not tree[i][j][k]%5:
                    for dx,dy in move:
                        nx=i+dx; ny=j+dy
                        if 0<=nx<n and 0<=ny<n:
                            tree[nx][ny].appendleft(1)
            ground[i][j]+=a[i][j]

for _ in range(k):
    ss()
    fw()

cnt = 0
for i in range(n):
    for j in range(n):
        cnt+=len(tree[i][j])
print(cnt)