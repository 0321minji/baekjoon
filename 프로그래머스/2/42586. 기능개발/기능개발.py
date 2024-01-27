import math
def solution(progresses, speeds):

    answer = [1]
    less=[(100-i) for i in progresses]
    day=[math.ceil(less[i]/speeds[i]) for i in range(len(progresses))]
    temp=day[0]

    for i in range(1,len(day)):
        if temp>=day[i]:
            answer[-1]+=1
        else:
            answer.append(1)
            temp=day[i]
        print(answer)
    return answer