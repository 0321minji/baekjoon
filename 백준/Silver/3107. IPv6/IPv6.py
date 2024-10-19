import sys
input=sys.stdin.readline

from collections import deque


ip=list(map(str,input().rstrip().split(':')))
cnt=8-len(ip)
#print(ip)
result=[]
check=False
for i in ip:
    length=len(i)
    #print(length)
    if length==0:
        if not check: 
            for _ in range(cnt+1):
                result.append('0000')
            check=True
        else:
            result.append('0000')
    else:
        temp='0'*(4-length)+i
        result.append(temp)

#print(result)
print(':'.join(result))
