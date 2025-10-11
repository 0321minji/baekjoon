from collections import Counter

def solution(N, stages):
    answer = []
    stage=Counter(stages)
    # print(stage)
    fail_rates=[]
    reached=len(stages)

    for s in range(1,N+1):
        stay = stage.get(s,0)
        #print(stay,reached)
        if not stay:
            fail=0
        else:
            fail=stay/reached
        fail_rates.append([s,fail])
        reached-=stay
    fail_rates.sort(key=lambda x:(-x[1]))

    for s,_ in fail_rates:
        answer.append(s)
    return answer