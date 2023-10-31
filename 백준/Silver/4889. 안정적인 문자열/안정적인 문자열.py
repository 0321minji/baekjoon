import sys
input=sys.stdin.readline

t=1
while True:
    result=0
    string=input().rstrip()
    if string.count('-')>=1:
        break
    
    st=1
    #처음과 마지막이 각각 닫는/여는 괄호면 무조건 교체 필요
    if string[0]=='}':
        result+=1
    if string[-1]=='{':
        result+=1
    
    for i in range(1,len(string)-1):
        if string[i]=='}':
            st-=1
            #닫는 괄호면 st-1 (앞이랑 짝)
        if string[i]=='{':
            #여는 괄호면 st+1 (뒤에 오는 거랑 짝 확인 필요)
            st+=1
        if st==-1:##닫는 괄호들이 연속적으로 나온 경우(값이 -1 됐을 때)
            result+=1
            st=1
    result+=st//2
    #s값들은 여는 남은 여는 괄호들의 갯수이므로 나누기 2한 만큼 교체 필요

    print(str(t)+'. '+str(result))
    t+=1
