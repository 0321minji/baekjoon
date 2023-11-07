from itertools import combinations
import sys
input=sys.stdin.readline

n=int(input())
num=[]

for i in range(1,11):
    for j in combinations(range(10),i):
        temp=''.join(map(str,reversed(list(j))))
        num.append(int(temp))
num.sort()
if n>=len(num):
    print(-1)
else:
    print(num[n])
