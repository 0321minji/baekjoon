import sys
input=sys.stdin.readline

n=int(input())
sn=[]
#1: 길이 짧은순, 2: 자리수합(숫자만), 3:사전순(숫자<알파벳)

for _ in range(n):
    temp=input().rstrip()
    num=0
    for i in range(len(temp)):
        if temp[i]<='9':
            num+=int(temp[i])
    sn.append([len(temp),num,temp])

sn.sort()
for i in range(n):
    print(sn[i][2])
