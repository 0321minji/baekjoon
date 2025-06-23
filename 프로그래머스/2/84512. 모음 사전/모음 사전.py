from itertools import product
def solution(word):
    answer = 0
    res=[]
    alp=['A','E','I','O','U','']
    for tmp in product(alp,repeat=5):
        res=list(set(res)|set(["".join(tmp)]))
    res.sort()
    answer=res.index(word)
    return answer