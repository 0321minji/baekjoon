def solution(n, t, m, p):
    answer = ''
    nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 진법의 첫 턴은 그대로 -> 그 다음부터는 각 자릿수를 하나씩 111 이면 3명이..
    # n진법 변환
    def get_num(n, q):
            rev_base = ''

            while n > 0:
                n, mod = divmod(n, q)
                rev_base += nums[mod]

            return rev_base[::-1]
    i=0    
    now='0'
    prev=0
    while i<=t*m:
        #i 번째에 말해야하는 수
        if now=='':
            prev+=1
            now=get_num(prev,n)
        # print(now)
        #i 번째가 튜브 차례면 answer+=
        if i%m==p-1:
            answer+=now[0]
            if len(answer)==t:
                break
        now=now[1:]
        i+=1
            
            
    return answer