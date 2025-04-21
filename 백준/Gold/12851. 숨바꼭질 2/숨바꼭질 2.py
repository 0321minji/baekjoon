import sys
input= sys.stdin.readline
from collections import deque

def bfs():
    que=deque([(n,0)])
    time=100001
    cnt=0
    visit=[100001]*(100001)
    visit[n]=0
    
    while que:
        now,t = que.popleft()
        if now==k:
            if t<time:
                time=t
                cnt=1
            elif t==time:
                cnt+=1
                
        for nxt in (now+1,now-1,now*2):
            if 0<=nxt<=100000: # 범위 안이고
                if visit[nxt] >= t+1: # 같거나 빠른 시간에 도달
                    visit[nxt]=t+1
                    que.append((nxt,t+1))
    print(time)
    print(cnt)
    
    
n,k=map(int,input().split())

bfs()
