import sys
input=sys.stdin.readline

n=int(input())
dots=[list(map(int,input().split())) for _ in range(n)]
temp=0

for i in range(n):
    if i==n-1:
        temp+=dots[i][0]*dots[0][1]-dots[i][1]*dots[0][0]
    else:
        temp+=dots[i][0]*dots[i+1][1]-dots[i][1]*dots[i+1][0]

print(round(0.5*abs(temp), 1))
