import sys
input=sys.stdin.readline

num=list(map(int,input().split()))
goal=int(input())

result=[]
num.sort()

for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==goal:
            if num[i]>=num[j]:
                result.append((num[j],num[i]))
            else:
                result.append((num[i],num[j]))
result.sort()

result=list(dict.fromkeys(result))

for i in result:
    print(*i)
print(len(result))
