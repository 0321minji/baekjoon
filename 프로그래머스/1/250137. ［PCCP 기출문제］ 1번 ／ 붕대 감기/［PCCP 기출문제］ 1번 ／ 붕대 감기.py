def solution(bandage, health, attacks):
    answer = 0
    time=list(attacks[i][0] for i in range(len(attacks)))
    #print(time)
    #print(time[-1]+1)
    c=0; h=health; m=bandage[0]; recover=bandage[1]; plus=bandage[2]
    #print(c,h,m,recover,plus)
    for i in range(1,time[-1]+1):
        if i in time: ##공격 받음
            c=0
            index=time.index(i)
            h-=attacks[index][1]
            if h<=0:
                h=-1
                break
        else:  #회복
            c+=1
            h+=recover
            if c==m:
                c=0;
                h+=plus
            h=min(h,health)
            if h<=0:
                h=-1
                break
        print(h)
    answer=h
    return answer