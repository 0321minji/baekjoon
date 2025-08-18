import sys
from itertools import permutations 
input=sys.stdin.readline

n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]

def simulations(lineup):
    index=0
    score=0
    for i in range(n):
        out=0
        base=0
        row=lst[i]
        while out<3:
            player=row[lineup[index]]
            if player==0:
                out+=1
            else:
                base=(base<<player)|(1<<(player-1))
                score+=(base>>3).bit_count()
                base&=0b111
            index=(index+1)%9
    return score
                
res=0
for lp in permutations(range(1,9)):
    lp=list(lp[:3])+[0]+list(lp[3:])
    res=max(res,simulations(lp))
print(res)            