from collections import deque
move=[[0,1],[0,-1],[1,0],[-1,0]]
def check(i,j,n,m,maps):
    que=deque([(i,j)])
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                que.append((nx,ny))
    return maps[n-1][m-1]  


def solution(maps):
    answer = 10**8
    n=len(maps)
    m=len(maps[0])

    temp=check(0,0,n,m,maps)
    if temp!=-1:
        answer=min(answer,temp)
    if answer==1:
        answer=-1
    return answer
