import sys
input=sys.stdin.readline
from collections import deque, defaultdict
from copy import deepcopy
n,L,R=map(int,input().split())
people=[list(map(int,input().split())) for _ in range(n)]

move=[(0,1),(0,-1),(1,0),(-1,0)]


# 열려있는지 안열려있는지 나뉘어서 열릴 수도 있음 -> 한 묶음에 어느 영역들이 속해있는지 알아야함

def calculate(country,count):
    res=count//len(country)
    for i,j in country:
        now[i][j]=res
    return
    
def check(i,j):
    # 연합 나라의 위치
    temp=[(i,j)] 
    # 연합의 인구수
    count=now[i][j]
    que=deque([(i,j)])
    while que:
        x,y=que.popleft()
        for dx,dy in move:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if L<=abs(now[x][y]-now[nx][ny])<=R:
                    visited[nx][ny]=True
                    count+=now[nx][ny]
                    temp.append((nx,ny))
                    que.append((nx,ny))
    if count!=now[i][j]:
        return temp,count
    return [],0
    
level=0
while True:
    index=0
    state=[]
    now=deepcopy(people)
    visited=[[False] *(n) for _ in range(n)]
    # print(visited)
    for i in range(n):
        for j in range(n):
            if  not visited[i][j]:
                visited[i][j]=True
                temp,count=check(i,j)
                if temp:
                    state.append((temp,count))
    # print(state,len(state[0][0]))
    if not state:
        break
    
    for country,count in state:
        calculate(country,count)
    level+=1
    people=now
    #print(state)
    #print(level,people)
    
    # if level==0:
    #     break
print(level)