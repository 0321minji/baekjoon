import sys
input=sys.stdin.readline

def solve(s):
    que=[]
    while(s):
        temp=s.pop(0)
        if temp=='(':
            que.append(temp)
        elif temp==')':
            if que:
                que.pop()
            else:
                return 'NO'

    if len(que)>0:
        return 'NO'
    return 'YES'

t=int(input())
for i in range(t):
    s=list(input())
    print(solve(s))
