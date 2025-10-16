from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    #외곽선 따라서 그래프 생성
    # 6,3 -> 5,3이 아니라 6,3-> 6,4 -> 5,4 -> 5,3이 최단거리임
    # 사각형 크기를 두배씩 키우고 답을 /2로 리턴
    # 제한 범위도 2배씩
    graph=[[-1 for _ in range(102)] for _ in range(102)]
    visited=[[1 for _ in range(102)] for _ in range(102)]

    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2,r)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                #내부
                if x1<i<x2 and y1<j<y2:
                    graph[i][j]=0
                #경계
                elif graph[i][j]!=0:
                    graph[i][j]=1
    # print(graph
    def bfs(x,y,a,b):
        que=deque([(x,y)])
        move=[(0,1),(0,-1),(1,0),(-1,0)]
        
        while que:
            i,j=que.popleft()
            
            if i==a and j==b:
                return visited[i][j]//2
            
            for di,dj in move:
                ni=i+di; nj=j+dj
                if graph[ni][nj]==1 and visited[ni][nj]==1:
                    visited[ni][nj]+=visited[i][j]
                    que.append((ni,nj))
        
    answer=bfs(characterX*2,characterY*2,itemX*2,itemY*2)       
        
    
    return answer