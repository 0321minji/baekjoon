from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    cars=defaultdict(int)
    inp=defaultdict(lambda:-1)
            
    for r in records:
        time, num, type=r.split(" ")
        h,m=time.split(":")
        t=60*int(h)+int(m)
        
        if type=='IN':
            inp[num]=t
        else:
            cars[num]+=t-inp[num]
            inp[num]=-1
            
    for num,value in inp.items():
        if value>=0:
            t=23*60+59
            cars[num]+=t-inp[num]
    print(cars)
    for k in sorted(cars.keys()):
        time=cars[k]
        temp=fees[1]
        if time>fees[0]:
            temp+=math.ceil((time-fees[0])/fees[2])*fees[3]
        answer.append(temp)
    return answer