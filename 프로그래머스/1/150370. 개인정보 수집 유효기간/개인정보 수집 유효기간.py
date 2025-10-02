def solution(today, terms, privacies):
    answer = []
    terms_dict={}
    for t in terms:
        type,month=t.split(' ')
        terms_dict[type]=int(month)
        
    def check(day,type):
        y,m,d=day.split('.')
        # 1년 = 12달 = 12*28 일
        # start 기준으로 type*28-1 만큼이랑 today 비교
        start = int(y)*12*28 + int(m)*28 + int(d) 
        t=terms_dict[type]*28-1
        return start+t
        
    y,m,d=today.split('.')
    today = int(y)*12*28+int(m)*28+int(d)
    
    
    for i,p in enumerate(privacies):
        start,type=p.split(' ')
        end = check(start,type)
        print(end,today)
        if end<today:
            answer.append(i+1)
        
    return answer