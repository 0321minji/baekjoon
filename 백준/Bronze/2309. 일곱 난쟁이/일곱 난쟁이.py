import sys
input=sys.stdin.readline
from itertools import permutations

h=[int(input()) for _ in range(9)]
h.sort()
for temp in permutations(h,7):
    if sum(list(temp))==100:
        result=list(temp)
        result.sort()
        print(*result,sep='\n')
        break
