import sys
from itertools import permutations

n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()

for i in permutations(nums,m):
    print(*i)
