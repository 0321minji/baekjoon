import sys
input=sys.stdin.readline

n=int(input())
result=dict()

for _ in range(n):
    a,b=map(str,input().split())

    if b=='enter':
        result[a]=b
    else:
        del result[a]

result=sorted(result.keys(), reverse=True)

print(*result,sep='\n')
