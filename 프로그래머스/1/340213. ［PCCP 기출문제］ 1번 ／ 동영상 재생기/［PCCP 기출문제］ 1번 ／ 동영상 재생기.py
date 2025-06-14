def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    sm,ss = map(int,op_start.split(':'))
    start = ss+sm*60
    em,es = map(int,op_end.split(':'))
    end = es+em*60
    lm,ls = map(int,video_len.split(':'))
    length = ls+lm*60
    pm,ps = map(int,pos.split(':'))
    n=ps+pm*60
    if start<=n<=end:
        n=end
        
    def move(now, cmd):
           
        # 10초 후
        if cmd == 'next':
            now = min(now+10,length)
            
        # 10초 전
        else:
            now = max(now-10,0)
        
        # 건너뛰기
        if start<=now<=end:
            return end
        return now
    
    def toStr(time):
        m=time//60
        if m<10:
            m='0'+str(m)
        else:
            m=str(m)
        n=time%60
        if n<10:
            n='0'+str(n)
        else:
            n=str(n)        
        return m+':'+n
    
    
    for c in commands:
        n=move(n,c)
    
    answer=toStr(n)

    return answer
