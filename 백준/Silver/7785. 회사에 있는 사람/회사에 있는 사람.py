import sys
input=sys.stdin.readline

n=int(input())
result={}
for _ in range(n):
    name,state=map(str,input().split())
    if name in result:
        result.pop(name)
    else:
        result[name]=1
result=list(result.keys())
result.sort(reverse=True)
print(*result, sep='\n')
