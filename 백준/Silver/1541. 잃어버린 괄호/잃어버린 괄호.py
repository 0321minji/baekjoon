import sys
input=sys.stdin.readline

## 최소를 만들기 위해 = -가 커야함 = - 있으면 그 뒤에 다 괄호로묶기?
## 뒤에서부터..?
string=input().rstrip()
num=[]
op=[]
temp=''
## 숫자랑 연산자 구분
for i in range(len(string)):
    if string[i] in ("+","-"):
        if not temp:
            op.append(string[i])
        else:
            num.append(int(temp))
            temp=''
            op.append(string[i])
    else:
        temp+=string[i]
num.append(int(temp))

result=0
temp=0
for i in range(len(op)-1,-1,-1):
    if op[i]=='+':
        temp+=num[i+1]
    elif op[i]=='-':
        temp+=num[i+1]
        result-=temp
        temp=0
    #print(result,i,num[i+1])
if temp:
    result+=temp
result+=num[0]
print(result)
