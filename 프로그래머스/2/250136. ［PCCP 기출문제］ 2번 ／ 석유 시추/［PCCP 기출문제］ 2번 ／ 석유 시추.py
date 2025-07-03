from collections import deque, defaultdict

# 모든 열에 대해서 탐색 -> 시간 초과날 듯..
# 덩어리를 기준으로 어떤 열에 해당하는지 기록해야할 듯
# 어떤 열 - 어떤 덩어리
# 어떤 덩어리 - 크기
move=[[0,1],[0,-1],[1,0],[-1,0]]
def solution(land):
    answer = 0
    n=len(land); m=len(land[0])
    rows=defaultdict(set)
    oils=defaultdict(int)
    
    def check(x,y,num):
        land[x][y]=num
        que=deque([(x,y)])
        rows[y]|=set([num-1])
        cnt=1
        while que:
            x,y=que.popleft()
            for dx,dy in move:
                nx=x+dx; ny=y+dy
                if (0<=nx<n and 0<=ny<m) and land[nx][ny]==1:
                    land[nx][ny]=num
                    cnt+=1
                    que.append((nx,ny))
                    rows[ny]|=set([num-1])
        oils[num-1]=cnt
    num=2
    # check(2,0,num)
    for i in range(m):
        for j in range(n):
            if land[j][i]==1:
                check(j,i,num)
                num+=1
    # print(land,rows,oils)
    
    for i in rows.keys():
        tmp=0
        for item in rows[i]:
            tmp+=oils[item]
        answer=max(answer,tmp)
            
        
            
        
    return answer