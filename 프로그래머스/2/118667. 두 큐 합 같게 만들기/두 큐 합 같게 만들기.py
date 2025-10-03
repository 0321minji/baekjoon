from collections import deque

def solution(queue1, queue2):
    res=0
    
    que1=deque(queue1)
    que2=deque(queue2)
    
    one = sum(que1)
    two = sum(que2)
    goal=(one+two)//2
    time = len(que1)+len(que2)
    
    if max(max(que1),max(que2))>goal:
        return -1
    
    while one!=goal:
        if res>time+2:
            return -1
        #print(one,two)
        if one>two:
            res+=1
            pop=que1.popleft()
            one-=pop
            two+=pop
            que2.append(pop)
            
        else:
            res+=1
            pop=que2.popleft()
            one+=pop
            two-=pop
            que1.append(pop)
            
    
    
    return res
    