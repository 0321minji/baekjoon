import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    sentence=list(input().strip())

    left=[]
    right=deque([])
    for i in range(len(sentence)):
        if sentence[i]==">":
            if right:
                temp=right.popleft()
                left.append(temp)
        elif sentence[i]=="<":
            if left:
                temp=left.pop()
                right.appendleft(temp)
        elif sentence[i]=="-":
            if left:
                left.pop()
        else:
            left.append(sentence[i])
    result=left+list(right)
    for i in range(len(result)):
        print(result[i],end='')
    print()
