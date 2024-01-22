import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    wear={}

    for _ in range(n):
        temp=list(input().split())
        t=temp[1]
        if t in wear:
            wear[t].append(temp[0])
        else:
            wear[t]=[temp[0]]
    result=1
    for i in wear:
        result*=(len(wear[i])+1)
    print(result-1)
