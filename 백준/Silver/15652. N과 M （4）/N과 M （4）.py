import sys
from collections import Counter

input=sys.stdin.readline

n,m=map(int,input().split())
number = [i for i in range(1,n+1)]
result=[0 for _ in range(m)]


#중복 조합
def combi_with_repeat(level,start):
    if level==m:
        print(*result)
        return

    for i in range(start,n):
        result[level]=number[i]
        combi_with_repeat(level+1,i)

combi_with_repeat(0,0)
