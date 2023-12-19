import sys
input=sys.stdin.readline

def bt(num):
    global cnt
    if len(n)==1:
        cnt+=1
        return
    L=set(list(num))
    if len(L)==1:
        cnt+=1
        return
    else:
        bt(num[1:])
        bt(num[:-1])
        
    
n=input().rstrip()
cnt=0
bt(n)
print(cnt)
