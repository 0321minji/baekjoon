from collections import deque
def solve(tree,visit,r):
    que=deque([r])
    visit[r]=1
    cnt=1
    while que:
        x=que.popleft()
        for i in tree[x]:
            if visit[i]==0:
                visit[i]=1
                que.append(i)
                cnt+=1
    return cnt

def solution(n, wires):
    answer = n
    tree=[[] for _ in range(n+1)]
    for a,b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    for a,b in wires:
        visit=[0]*(n+1)

        tree[a].remove(b)
        tree[b].remove(a)
        
        answer=min(abs(solve(tree,visit,a)-solve(tree,visit,b)),answer)
        
        tree[a].append(b)
        tree[b].append(a)
        
    return answer