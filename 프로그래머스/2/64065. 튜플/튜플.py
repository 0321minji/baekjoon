from collections import defaultdict

def solution(s):
    answer = []
    tup=defaultdict(int)
    
    n=len(s)
    num=''
    for i in range(n):
        if s[i]=='{':
            temp=[]
        elif s[i].isnumeric():
            num+=s[i]
        elif s[i]==',':
            if s[i-1].isnumeric():
                temp.append(int(num))
                num=''
        else:
            if num:
                temp.append(int(num))
            num=''
            for t in temp:
                tup[t]+=1
    tup=sorted(tup.items(),key=lambda x:-x[1])
    for t in tup:
        answer.append(t[0])
    return answer