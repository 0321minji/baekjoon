import sys
input=sys.stdin.readline
from collections import Counter

n,m=map(int,input().split())
dna=list(input().rstrip() for _ in range(n))
index=list(zip(*dna))

## s 찾기
def find(index):
    result=''
    for i in range(m):
        temp=index[i]
        counter=Counter(temp)

        sorting = sorted(counter.items(),key=lambda x: (-x[1], x[0]))
        result+=sorting[0][0]
    return result

## 계산하기
def cal(result,index):
    cnt=0
    for i in range(m):
        cnt+=(n-index[i].count(result[i]))
    print(result)
    print(cnt)
    

result = find(index)
cal(result,index)

