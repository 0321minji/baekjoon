from collections import deque
move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve(i,j,maps):
    que=deque([])
    que.append((i,j))
    
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx=x+dx; ny=y+dy
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                que.append((nx,ny))
    return maps[len(maps)-1][len(maps[0])-1]
        

def solution(maps):
    answer = solve(0,0,maps)
    
    return answer if answer!=1 else -1