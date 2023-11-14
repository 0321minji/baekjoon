import sys
from collections import deque
input=sys.stdin.readline

def solve():
    que=deque([])
    while rumor:
        index=rumor.popleft()
        temp=people[index]
        for i in temp:
            if time[i]!=-1:
                continue
            count=0
            for k in range(len(people[i])):
                if time[people[i][k]]!=-1:
                    count+=1
            if len(people[i])>count*2:
                continue
            que.append(i)
        #해당 시간에 대한 탐색이 끝
        if not rumor:
            while que:
                tmp=que.popleft()
                time[tmp]=time[index]+1
                rumor.append(tmp)
    print(*time[1:])

n=int(input())
people=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    people.append(temp[:-1])

people.insert(0,[])
m=int(input())
rumor=list(map(int,input().split()))

time=[-1]*(n+1)
for i in rumor:
    time[i]=0

rumor=deque(rumor)
solve()
