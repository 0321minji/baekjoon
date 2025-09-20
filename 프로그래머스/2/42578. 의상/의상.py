from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_map = defaultdict(int)
    for name , type in clothes:
        clothes_map[type]+=1
    
    print(clothes_map.keys())
    for a in clothes_map.values():
        answer*=(a+1)

        
    return answer-1