import sys, copy
input = sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(h,i,j,graph):
    que=[(i,j)]
    while que:
        x,y=que.pop()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>h:
                que.append((nx,ny))
                graph[nx][ny]=0
                
            
def solve(h,graph):
    result=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h:
                result+=1
                graph[i][j]=0
                bfs(h,i,j,graph)

                
    return result
    

n=int(input())
rain=[list(map(int,input().split())) for _ in range(n)]

high=max(map(max,rain))
result=0

for h in range(high):
    #result=max(result,solve(h,rain))
    temp=copy.deepcopy(rain)
    result=max(result,solve(h,temp))
    
print(result)
