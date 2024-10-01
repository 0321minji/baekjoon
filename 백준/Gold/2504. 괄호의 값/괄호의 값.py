import sys
input= sys.stdin.readline

string=list(input().rstrip())
# print(string)

st=[]
tmp=1
result=0
for i in range(len(string)):
    if string[i]=='(':
        tmp*=2
        st.append(string[i])
    elif string[i]==')':
        if not st or st[-1] == '[':
            print(0)
            exit()
        if string[i-1]=='(':
            result+=tmp
        st.pop()       
        tmp//=2 
    elif string[i]=='[':
        tmp*=3
        st.append(string[i])
    elif string[i]==']':
        if not st or st[-1]=='(':
            print(0)
            exit()
        if string[i-1]=='[':
            result+=tmp
        st.pop()
        tmp//=3    
    #print(string[i])
if st :
    result=0
print(result)
