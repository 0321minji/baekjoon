import sys
input=sys.stdin.readline
from collections import deque

def solve(t):
    left=[]
    right=deque([])
    t=deque(t)
    index=0
    while t:
        temp=t.popleft()
        if temp=='<':
            if left:
                #right.appendleft(left.pop())
                right.append(left.pop())
        elif temp=='>':
            if right:
                left.append(right.pop())
        elif temp=='-':
            if left:
                left.pop()
        else:
            left.append(temp)
        #print(left,right)
    return left+list(right)[::-1]
    
    
n=int(input())
for i in range(n):
    t=list(input().rstrip())
    print(*solve(t),sep='')
    
