import sys
sys.setrecursionlimit(10**7)
move=[[1,0],[-1,0],[0,1],[0,-1],[0,0]]
#방문체크 나눠서
#동시에 방문 안되는것도 ..
#서로의 직전위치로 스위치 불가

answer = 10**9
def solution(maze):
    n=len(maze); m=len(maze[0])
    red_v=[[0]*m for _ in range(n)]
    blue_v=[[0]*m for _ in range(n)]
    def check(cnt,red_now,blue_now,red_v,blue_v):
        global answer
        
        if cnt>=answer:
            return
        if red_now == red_goal and blue_now == blue_goal:
            answer=min(answer,cnt)
            
        for (dx,dy) in move:
            nx=red_now[0]+dx; ny=red_now[1]+dy;
            if (nx<0 or nx>=n or ny<0 or ny>=m) or (maze[nx][ny]==5) or red_v[nx][ny] and not (red_goal==(nx,ny)):
                continue
            red_v[nx][ny]=1
            for (ddx,ddy) in move:
            ## 둘다 그대로 X
                if(dx,dy)==(0,0) and (ddx,ddy)==(0,0):
                    continue
                bx=blue_now[0]+ddx; by=blue_now[1]+ddy;
                #기본 탐색 조건
                if (bx<0 or bx>=n or by<0 or by>=m) or (maze[bx][by]==5) or ((blue_v[bx][by]) and (blue_goal!=(bx,by))):
                    continue
                    #print(nx,ny,bx,by)
                    #스위치 x, 동시 x
                if (nx==bx and ny==by) or (red_now == (bx,by) and blue_now == (nx,ny)):
                    continue
                blue_v[bx][by]=1
                check(cnt+1,(nx,ny),(bx,by),red_v,blue_v)
                blue_v[bx][by]=0
            red_v[nx][ny]=0
            
    ## 시작점 & 끝점
    for i in range(n):
        for j in range(m):
            if maze[i][j]==1:
                red_now=(i,j)
                red_v[i][j]=1
            elif maze[i][j]==2:
                blue_now=(i,j)
                blue_v[i][j]=1
            elif maze[i][j]==3:
                red_goal=(i,j)
            elif maze[i][j]==4:
                blue_goal=(i,j)
    
    check(0,red_now,blue_now,red_v,blue_v)
    if answer == 10**9:
        return 0
    
    return answer