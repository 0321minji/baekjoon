import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
do=deque()
su=deque()
for i in range(n):
    a,b=map(int,input().split())
    do.append(a)
    su.append(b)

dog=[]
sug=[]
index=1
for i in range(m):
    index=(index+1)%2

    if index==0:
        if do:
            dog.append(do.pop())
    else:
        if su:
            sug.append(su.pop())
    if not do:
        print('su')
        exit()
    if not su:
        print('do')
        exit()       
    if dog and sug and dog[-1]+sug[-1]==5:
        #수연 종
        su.extendleft(dog)
        su.extendleft(sug)
        dog=deque()
        sug=deque()
    elif (dog and dog[-1]==5) or (sug and sug[-1]==5):
        do.extendleft(sug)
        do.extendleft(dog)
        dog=deque()
        sug=deque()

        
if len(do)>len(su):
    print('do')
elif len(do)<len(su):
    print('su')
else:
    print('dosu')
    
        
