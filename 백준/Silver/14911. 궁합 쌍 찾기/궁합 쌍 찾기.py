import sys
input=sys.stdin.readline

innum=list(map(int,input().split()))
goal=int(input())

result=[]
innum.sort()

for i in range(len(innum)-1):
    for j in range(i+1,len(innum)):
        if innum[i]+innum[j]==goal:
            if innum[i]>=innum[j]:
                result.append((innum[j],innum[i]))
            else:
                result.append((innum[i],innum[j]))
result.sort()
result=list(dict.fromkeys(result))

for temp in result:
    print(*temp)
print(len(result))
