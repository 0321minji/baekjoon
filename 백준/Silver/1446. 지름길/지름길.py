import sys
input=sys.stdin.readline

n,d=map(int,input().split())
load=[]

for i in range(n):
    load.append(list(map(int,input().split())))

load.sort()
temp=[i for i in range(d+1)]

for i in load:
    s,e,l=i
    if e<=d:
        temp[e]=min(temp[s]+l,temp[e])
    for j in range(s,d+1):
        temp[j]=min(temp[j-1]+1,temp[j])

print(temp[d])
