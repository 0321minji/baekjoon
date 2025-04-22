import sys
input=sys.stdin.readline
from collections import defaultdict


def calc():
    res=1
    key = c.keys()
    for k in key:
        res=res*(len(c[k])+1)
    print(res-1)


t=int(input())
for _ in range(t):
    n=int(input())
    c=defaultdict(list)
    for _ in range(n):
        a,b=map(str,input().split())
        c[b].append(a)
    calc()
