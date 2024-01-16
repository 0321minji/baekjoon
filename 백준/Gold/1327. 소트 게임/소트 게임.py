import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    que=deque([])
    visit=set(''.join(num))
    que.append((num,0))
    
    while que:
        s,cnt=que.popleft()
        if s==result:
            return cnt
        for i in range(n-k+1):
           temp=s[i:i+k]
           temp.reverse()
           tmp=s[:i]+temp+s[i+k:]
           st=''.join(tmp)
           if st not in visit:
               que.append((tmp,cnt+1))
               visit.add(st)

    if ''.join(result) not in visit:
        return -1
    return cnt

n,k=map(int,input().split())
num=list(input().split())
result=sorted(num)

print(bfs())
