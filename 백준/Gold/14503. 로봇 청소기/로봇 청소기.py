import sys
input=sys.stdin.readline

def solve(graph,x,y,d):
    answer=0
    move=[[-1,0],[0,1],[1,0],[0,-1]]
    while 1:
        if graph[x][y]==0:
            answer+=1
            graph[x][y]=2

        for _ in range(4):
            d=(d+3)%4
            nx=x+move[d][0]
            ny=y+move[d][1]
            if graph[nx][ny]==0:
                x=nx
                y=ny
                break
        else:
            nd=(d+2)%4
            nx=x+move[nd][0]
            ny=y+move[nd][1]
            if graph[nx][ny]==1:
                break
            x=nx
            y=ny
    return answer



n,m=map(int,input().split())
r,c,d=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))


print(solve(graph,r,c,d))
