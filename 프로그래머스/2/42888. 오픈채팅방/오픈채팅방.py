def solution(record):
    answer = []
    user={}
    state=[]
    
    for e in record:
        e=e.split()
        st=e[0]; i=e[1]
        
        if st =='Enter' or st=='Change':
            user[i]=e[2]
        state.append((st,i))
    
    for info in state:
        st , i = info
        if st =='Enter':
            answer.append(user[i]+'님이 들어왔습니다.')
        elif st=='Leave':
            answer.append(user[i]+'님이 나갔습니다.')
    
    
    return answer