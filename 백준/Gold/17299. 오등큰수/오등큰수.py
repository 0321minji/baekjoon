import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))

cnt=Counter(num)
#등장횟수'
f=[cnt[i] for i in num]
m=max(f)
result=[-1]*n

st=[0]
i=1
while st and i<n:
    while st and f[st[-1]]<f[i]:
        result[st[-1]]=num[i]
        st.pop()
    st.append(i)
    i+=1

print(*result)
