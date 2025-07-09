import math

def solution(r1, r2):
    answer = 0
    
    # r1<=루트(x^2+y^2)<=r2인 x,y
    def count():
        cnt=0

        for x in range(1,r2+1):
            max_sq = r2**2 - x**2
            min_sq = r1**2 - x**2
            if max_sq <0:
                break
            y_min = math.ceil(math.sqrt(min_sq)) if min_sq>0 else 0
            y_max = math.floor(math.sqrt(max_sq))
            cnt+=max(0,y_max-y_min+1)
        return cnt
    
    answer+=count()*4

    return answer