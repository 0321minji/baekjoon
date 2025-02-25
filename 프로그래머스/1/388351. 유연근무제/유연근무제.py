def solution(schedules, timelogs, startday):
    answer = 0
    # i = 사람

    for i in range(len(schedules)):
        flag=True
        goal=schedules[i]
        hour=goal//100
        mini=goal%100
        
        gm = (mini+10)%60
        if mini>=50:
            gh=hour+1
        else:
            gh=hour
        day=startday
        for j in range(7):
            temp=startday+j
            if temp>=8:
                temp-=7
            if temp in [1,2,3,4,5]:
                today = timelogs[i][j]
                hh = today//100
                mm = today%100
                if hh>gh:
                    flag=False
                    break
                if hh==gh and mm>gm:
                    flag=False
                    break
        if flag:
            answer+=1

    return answer