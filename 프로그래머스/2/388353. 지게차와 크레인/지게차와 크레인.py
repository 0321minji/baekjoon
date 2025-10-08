from collections import deque

# cnt=0
def solution(storage, requests):
    answer=0
    
    for i in range(len(storage)):
        storage[i]=[-1]+list(storage[i])+[-1]
    n=len(storage[0])
    storage=[[-1]*n]+storage+[[-1]*n]
    print(storage)
    
    n=len(storage)
    m=len(storage[0])
    
    # 접근 가능한 컨테이너
    def outline(r):
        global cnt

        temp=[]
        for i in range(n):
            for j in range(m):
                if storage[i][j]==r:
                    for x,y in ([i+1,j],[i,j-1],[i-1,j],[i,j+1]):
                        if 0<=x<n and 0<=y<m and storage[x][y]==-1:
                            temp.append([i,j])
                            # cnt+=1
        for x,y in temp:
            storage[x][y]=-1
    # 모든 컨테이너
    def inline(r):
        global cnt
        temp=[]
        
        for i in range(n):
            for j in range(m):
                if storage[i][j]==r:
                    temp.append([i,j])

        for i,j in temp:
            flag=False
            for x,y in ([i+1,j],[i,j-1],[i-1,j],[i,j+1]):
                if 0<=x<n and 0<=y<m and storage[x][y]==-1:
                    storage[i][j]=-1
                    flag=True
            if not flag:
                storage[i][j]=-2    
    

    NEI = [(1,0), (-1,0), (0,1), (0,-1)]

    def relax_minus2():
        # -1에 인접한 -2들을 큐에 넣고, -1로 승격시키며 연쇄 전파
        q = deque()
        # 초기 시드 수집
        for i in range(n):
            for j in range(m):
                if storage[i][j] == -2:
                    for dx, dy in NEI:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < m and storage[x][y] == -1:
                            q.append((i, j))
                            break

        # BFS 전파
        while q:
            i, j = q.popleft()
            if storage[i][j] != -2:
                continue  # 이미 처리된 경우 스킵
            # 여전히 -1 이웃이 있는지 최종 확인
            for dx, dy in NEI:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and storage[x][y] == -1:
                    storage[i][j] = -1  # 승격
                    # 이 승격으로 주변 -2들이 새롭게 접근 가능해질 수 있으니 큐에 추가
                    for dx2, dy2 in NEI:
                        xx, yy = i + dx2, j + dy2
                        if 0 <= xx < n and 0 <= yy < m and storage[xx][yy] == -2:
                            q.append((xx, yy))
                    break

    for r in requests:
        if len(r)==1:
            outline(r)
        else:
            inline(r[0])
        relax_minus2()
        
    print(storage)
    
    for s in storage:
        for i in s:
            if not isinstance(i, int):
                answer+=1
    return answer