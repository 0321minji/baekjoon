import math
def solution(begin, end):
    answer = []
    
    def find(n):
        if n==1:
            return 0
        l=int(math.sqrt(n))
        # l=min(l,10000000)
        tmp=0
        for i in range(1,l+1):
            if n%i==0:
                if tmp<=10000000:
                    tmp=i
                    if n//i!=i and n//i!=n:
                        if n//i<=10000000:
                            return n//i
        return tmp
    
    for i in range(begin,end+1):
        answer.append(find(i))
    return answer