import sys
from collections import deque
input=sys.stdin.readline

def solve():
    result='<'
    index=0
    while people:
        index+=k-1
        index=index%len(people)
        result+=str(people.pop(index))+', '
    result=result[:-2]+'>'
    print(result)
    
n,k=map(int,input().split())
people=[i for i in range(1,n+1)]
solve()
