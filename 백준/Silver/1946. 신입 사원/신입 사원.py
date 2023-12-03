import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    score=[]
    n=int(input())
    score=[list(map(int,input().split())) for _ in range(n)]
    score.sort()
    temp=score[0][1]
    result=1
    for i in range(1,n):
        if score[i][1]<temp:
            result+=1
            temp=score[i][1]
    print(result)
