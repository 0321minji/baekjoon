import sys
from collections import Counter
input=sys.stdin.readline

def solve():
    st=[]
    for i in fx:
        if i.isalpha():
            print(i,end='')
            
        elif i=='(':
            st.append('(')
            
        elif i=='*' or i=='/':
            while st and (st[-1]=='*' or st[-1]=='/'):
                print(st.pop(),end='')
            st.append(i)
            
        elif i=='+' or i=='-':
            while st and st[-1]!='(':
                print(st.pop(),end='')
            st.append(i)
            
        else:
            while st and st[-1]!='(':
                print(st.pop(),end='')
            st.pop()
    while st:
        print(st.pop(),end='')

fx=list(input().rstrip())
solve()
