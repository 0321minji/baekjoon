import itertools

def solution(friends, gifts):
    answer = 0
    giftMap={}
    giftCount = {}
    result={}
    for i in friends:
        giftCount[i]=[0,0,0]
        giftMap[i]={j:0 for j in friends }
        result[i]=0
        
    for gift in gifts:
        a,b=gift.split(' ')
        giftMap[a][b]+=1
        giftCount[a][0]+=1
        giftCount[b][1]+=1
        giftCount[a][2]+=1
        giftCount[b][2]-=1
    
    def cal():
        for i,j in itertools.combinations(friends,2):
            if i==j:
                continue
            if giftMap[i][j]<giftMap[j][i]:
                result[j]+=1
            elif giftMap[i][j]>giftMap[j][i]:
                result[i]+=1
            else:
                if giftCount[i][2] > giftCount[j][2]:
                    result[i]+=1
                elif giftCount[i][2]<giftCount[j][2]:
                    result[j]+=1
    cal()
    answer=max(list(result.values()))
            
                

    return answer

# 일단 선물 지수 계산 및 ㅌ예제 처럼 그래프로 저장? 지수 # dictionary 사용
# [i][j] a 랑 [j][i] b 비교 a>b 이면 j -> i 저장에게 주기   반대 i->j저장에게
# ij 두번 씩 비교 안해도 됨..
# a= b같으면 -> 선물지수 비교 -> 같으면 pass 
# 결과도 그래프에 저장 (다음 달의 선물 지수) ? (이름 - 받은 선물)
# 받은 선물마 저장하며 됨 
