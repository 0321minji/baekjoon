from collections import deque

def solution(priorities, location):
    answer = 0
    pr=deque([])
    for i in range(len(priorities)):
        pr.append((priorities[i],i))
    priorities.sort()
    cnt=1
    while pr:
        temp=pr.popleft()
        if temp[0]>=priorities[-1]:
            priorities.pop()
            if temp[1]==location:
                return cnt
            cnt+=1
        else:
            pr.append((temp))

    return answer