import sys
input=sys.stdin.readline
from itertools import product

n,m=map(int,input().split())
graph=[list(map(str,input().split())) for _ in range(n)]
cctv=[]
visit = [row[:] for row in graph]
move=[(0,1),(1,0),(0,-1),(-1,0)]
res=0


def check(x,y,direct):
    dir=direct%4
    dx,dy=move[dir]
    while 0<=x<n and 0<=y<m:
        x+=dx; y+=dy
        if not (0 <= x < n and 0 <= y < m):
            break
        if visit[x][y]=='6':
            break
        if visit[x][y]=='0':
            visit[x][y]='#'
                   
def cnt(visit):
    tmp=0
    for i in range(n):
        for j in visit[i]:
            if j=='0':
                tmp+=1
    return tmp

for i in range(n):
    for j in range(m):
        if '1'<=graph[i][j]<='5':
            cctv.append([graph[i][j],i,j])
        elif graph[i][j]=='0':
            res+=1

k=len(cctv)
for case in product([0,1,2,3],repeat=k):
    visit = [row[:] for row in graph]
    #print(case)
    #cctv 번호와 방향
    for index, direct in enumerate(case):
        num,x,y=cctv[index]
        num=int(num)
        if num==1:
            check(x,y,direct)
        elif num==2:
            check(x,y,direct)
            check(x,y,direct+2)
        elif num==3:
            check(x,y,direct)
            check(x,y,direct+1)
        elif num==4:
            check(x,y,direct)
            check(x,y,direct+1)
            check(x,y,direct+2)
        else:
            check(x,y,direct)
            check(x,y,direct+1)
            check(x,y,direct+2)
            check(x,y,direct+3)
    
    res=min(res,cnt(visit))

print(res)