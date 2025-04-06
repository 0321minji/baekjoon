import sys
input= sys.stdin.readline

n=int(input())
p=[]

for _ in range(n):
    p.append(list(map(int,input().split())))

for i in p:
    cnt=1
    for j in p:
        if i[0]<j[0] and i[1]<j[1]:
            cnt+=1
    print(cnt,end=" ")
