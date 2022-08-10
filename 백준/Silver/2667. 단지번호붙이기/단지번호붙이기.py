from collections import deque

move=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y):
    n=len(graph)
    que=deque([])
    que.append((x,y)) #탐색 시작점
    graph[x][y]=0
    count=1

    while(que):
        a,b=que.popleft()
        for i in move:
            nx=a+i[0]
            ny=b+i[1]
            if nx<0 or nx>=n or ny<0 or ny>=n: #범위 벗어나면
                continue
            if graph[nx][ny]==1: #다음 인접한 위치가 1이면
                graph[nx][ny]=0
                que.append((nx,ny))
                count+=1
    return count

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in result:
    print(i)