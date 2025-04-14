import sys
input=sys.stdin.readline

n=int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
xy.sort()

for t in xy:
    print(*t)