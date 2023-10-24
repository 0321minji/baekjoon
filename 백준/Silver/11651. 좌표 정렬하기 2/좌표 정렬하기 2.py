####
# 1. y좌표 기준 정렬 
# 2. x좌표 기준 정렬
####
import sys
input=sys.stdin.readline

n=int(input())
num=[]
for _ in range(n):
    num.append(list(map(int,input().split())))

num=sorted(num, key=lambda x: (x[1],x[0]))

for i in num:
    print(*i,end='\n')
    
