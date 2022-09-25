import sys
input=sys.stdin.readline
from collections import deque
def solve(s):
    left=[]
    right=[]
    s=deque(s)
    while s:
        temp=s.popleft()
        if temp=='-':
            if left:
                left.pop()
        elif temp=='<':
            if left:
                right.append(left.pop())
        elif temp=='>':
            if right:
                left.append(right.pop())
        else:
            left.append(temp)
    return left+right[::-1]

t=int(input())
for i in range(t):
    s=list(input().strip())
    print(*solve(s),sep='')
