import sys
from collections import Counter
input=sys.stdin.readline

def solve():
    st=[]
    for i in range(len(f)):
        if 'A'<=f[i]<='Z':
            print(f[i],end='')
        elif f[i]=='(':
            st.append('(')
        elif f[i]=='*' or f[i]=='/':
            while st and (st[-1]=='*' or st[-1]=='/'):
                    print(st.pop(),end='')
            st.append(f[i])
        elif f[i]=='+' or f[i] =='-':
            while st and st[-1]!='(':
                    print(st.pop(),end='')
            st.append(f[i])
        else:
            while st and st[-1]!='(':
                print(st.pop(),end='')
            st.pop()
    while st:
        print(st.pop(),end='')

f=list(input().rstrip())
solve()
