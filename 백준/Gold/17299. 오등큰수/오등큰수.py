import sys
from collections import Counter
input=sys.stdin.readline

def solve(f):
    st=[0]
    i=0
    result=[-1]*n
    while st and i<n:
        while st and f[st[-1]]<f[i]:
            result[st[-1]]=a[i]
            st.pop()
        st.append(i)
        i+=1

    return result

n=int(input())
a=list(map(int,input().split()))
cnt=Counter(a)
f=[cnt[i] for i in a]

print(*solve(f))
