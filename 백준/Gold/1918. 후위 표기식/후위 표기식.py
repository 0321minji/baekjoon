import sys
input=sys.stdin.readline

inp=list(input().rstrip())
st=[]
result=''

for temp in inp:
    if temp.isalpha():
        result+=temp

    elif temp=='(':
        st.append(temp)

    elif temp =='*' or temp=='/':
        while st and (st[-1]=='*' or st[-1]=='/'):
            result+=st.pop()
        st.append(temp)

    elif temp=='+' or temp== '-':
        while st and st[-1]!='(':
            result+=st.pop()
        st.append(temp)

    elif temp==')':
        while st and st[-1]!='(':
            result+=st.pop()
        st.pop()

while st:
    result+=st.pop()
print(result)