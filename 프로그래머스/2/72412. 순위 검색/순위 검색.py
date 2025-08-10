from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []

    dic=defaultdict(list)
    for i in info:
        temp=list(map(str,i.split(' ')))
        k=temp[:-1]
        score=int(temp[-1])
        for r in range(5):  # 0~4개 유지 (총 16가지)
            for comb in combinations(range(4), r):
                key = []
                for i in range(4):
                    key.append(k[i] if i in comb else '-')
                dic[' '.join(key)].append(score)           
    
    for lst in dic.values():
        lst.sort()

    for q in query:
        q = q.replace(' and ', ' ')
        a, b, c, tail = q.split(' ', 3)
        d, min_score = tail.rsplit(' ', 1)
        key = f"{a} {b} {c} {d}"
        people=dic[key]
        answer.append(len(people)-bisect_left(people,int(min_score)))
    
    return answer