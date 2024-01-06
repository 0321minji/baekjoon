import sys
input = sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y,cnt):
    que=[(x,y)]

    while que:
        x,y=que.pop()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
                    que.append((nx,ny))
                    graph[nx][ny]=0
                    cnt+=1
                    
    return cnt

n=int(input())
graph=[list(map(int,list(input().rstrip()))) for _ in range(n)]
result=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            graph[i][j]=0
            result.append(bfs(i,j,1))

print(len(result))
result.sort()
print(*result,sep='\n')
