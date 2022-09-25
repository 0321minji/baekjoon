import sys
input=sys.stdin.readline

s=list(input().strip())
que=0
ans=0

for i in range(len(s)):
    temp=s[i]
    if temp=='(':
        que+=1
    else:
        if i>0 and s[i-1]=='(':
            que-=1
            ans+=que
        else:
            que-=1
            ans+=1
print(ans)
        