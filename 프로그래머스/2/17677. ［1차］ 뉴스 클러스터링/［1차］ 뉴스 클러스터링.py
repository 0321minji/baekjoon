from collections import defaultdict
def solution(str1, str2):
    answer = 0
    A=defaultdict(int)
    B=defaultdict(int)
    
    def make_set(string,s):
        string=string.lower()
        for i in range(len(string)-1):
            if 'a'<=string[i]<='z' and 'a'<=string[i+1]<='z':
                s[string[i]+string[i+1]]+=1
    
    def get_score():
        s=list(set(list(A.keys())+list(B.keys())))
        union=inter=0

        for key in s:
            tA=A[key]
            tB=B[key]
            if tA and tB:
                union+=max(tA,tB)
                inter+=min(tA,tB)
            else:
                union+=tA+tB
        return inter/union if union!=0 else 1
    
    make_set(str1,A)
    make_set(str2,B)
    # print(A,B)
    score=get_score()
    # print(inter,union)
    
    
    return int(score*65536)

# aa aa
# aa aa aa
# 교집합 (aa,aa)
# 합집합 (aa,aa,aa)
# 