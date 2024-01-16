from collections import deque
def check(node , visit, computers,n):
    q=deque([node])
    
    while q:
        temp=q.popleft()
        for i in range(n):
            if temp!=i and computers[temp][i] and not visit[i]:
                visit[i]=1
                q.append(i)
            

def solution(n, computers):
    answer = 0
    visit=[0]*(n)
    for i in range(n):
        if not visit[i]:
            visit[i]=1
            check(i,visit,computers,n)
            answer+=1
    
    return answer