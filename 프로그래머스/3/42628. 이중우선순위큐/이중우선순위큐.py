from collections import deque
def solution(operations):
    answer = []
    que=deque([])
    
    for o in operations:
        op,num=o.split(' ')
        num=int(num)
        if op=='I':
            que.append(num)
            que=deque(sorted(list(que)))
        if op=='D':
            if num==1 and que:
                que.pop()
            elif num==-1 and que:
                que.popleft()
    if que:
        a=que.popleft()
        b=que.pop()
        return [b,a]
    else:
        return [0,0]
        
    return answer