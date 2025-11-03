from itertools import permutations
def solution(k, dungeons):
    answer = -1
    n=len(dungeons)
    for i in permutations([i for i in range(n)],n):
        t=k
        res=0
        for index in i:
            if t>=dungeons[index][0]:
                t-=dungeons[index][1]
                res+=1
        answer=max(answer,res)
    
    return answer