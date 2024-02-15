from collections import deque

def solution(operations):
    answer = []
    que=deque([])
    for o in operations:
        op,n=o.split(' ')
        n=int(n)
        if op=='I':
            que.append(n)
            que=deque(sorted(list(que)))
        elif n==-1 and que:
            que.popleft()
        elif que:
            que.pop()
    if que:
        return [que.pop(),que.popleft()]
    
    return [0,0]