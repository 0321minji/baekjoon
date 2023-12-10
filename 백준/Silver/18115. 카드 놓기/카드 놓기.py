import sys
from collections import deque
input=sys.stdin.readline

def solve(n,a):
    card=1
    result=deque([])
    for i in range(n-1,-1,-1):
        if a[i]==1:
            result.appendleft(card)
        elif a[i]==2:
            result.insert(1,card)
        else:
            result.append(card)
        card+=1
    return result

n=int(input())
a=list(map(int,input().split()))
print(*solve(n,a))
