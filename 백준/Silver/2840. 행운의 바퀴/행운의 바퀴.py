import sys
n,k=map(int,input().split())

circle=[0]*(n)
index=0
for i in range(k):
    num,al=map(str,input().split())
    index=(index-int(num))%n
    if circle[index]==0:
        if al in circle:
            circle[index]=-1
            break
        circle[index]=al
    else:
        if circle[index]==al:
            continue
        circle[index]=-1

circle=circle[index:]+circle[:index]
if -1 in circle:
    print('!')
else:
    for i in circle:
        if i==0:
            print("?",end='')
        else:
            print(i,end='')
