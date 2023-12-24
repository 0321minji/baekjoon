import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(1,11):
    for j in combinations(range(10),i):
        j=list(j)
        j.sort(reverse=True)
        temp=''.join(map(str,j))
        num.append(int(temp))
num.sort()
if n>=len(num):
    print(-1)
else:
    print(num[n])
