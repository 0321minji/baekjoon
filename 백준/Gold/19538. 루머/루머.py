import sys
from collections import deque
input=sys.stdin.readline

move=[[0,1],[0,-1],[1,0],[-1,0]]

def solve():
    que=deque(rumor)
    while que:
        index=que.popleft()
        fr=people[index]
        for i in fr:
            if i==-1:
                continue
            if time[i]>=0:
                continue
            if index in people[i]:
                people[i].remove(index)
                people[i].append(-1)
            #print(i,people[i],people[i].count(-1),len(people[i]))
            
            if people[i].count(-1)>=((len(people[i])+1)//2):
                time[i]=time[index]+1
             #   print(time,i,index)
                que.append(i)
            
n=int(input())
people=[[] for _ in range(n+1)]
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    people[i]=temp[:-1]

m=int(input())
rumor=list(map(int,input().split()))
time=[-1]*(n+1)

for i in rumor:
    time[i]=0

solve()
print(*time[1:])
