from collections import deque
def solve(n,i,visit,computers):
    visit[i]=1
    que=deque([])
    que.append(i)
    
    while que:
        temp=que.popleft()
        visit[temp]=1
        for j in range(n):
            if j!=temp and computers[temp][j]==1 and not visit[j]:
                visit[j]=1
                que.append(j)
    
def solution(n, computers):
    answer = 0
    visit=[0]*(n)
    for i in range(n):
        if not visit[i]:
            solve(n,i,visit,computers)
            answer+=1
    
    return answer