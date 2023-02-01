import sys
input=sys.stdin.readline

def onoff(i):
    switch[i]=(switch[i]+1)%2
    return

n=int(input())
switch=[-1]+list(map(int,input().split()))
st=int(input())

for _ in range(st):
    s,num=map(int,input().split())
    if s==1:
        for i in range(num,n+1,num):
            onoff(i)
    else:
        onoff(num)
        for j in range(n//2):
            if num+j>n or num-j<1:
                break
            if switch[num+j]==switch[num-j]:
                onoff(num+j)
                onoff(num-j)
            else:
                break

switch=switch[1:]
for i in range(len(switch)):
    if i%20==0 and i>0:
        print()
    print(switch[i],end=' ')
