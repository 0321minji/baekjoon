def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    
    #시작점
    bridge=set([costs[0][0]])
    
    # 크루스칼
    while len(bridge)!=n:
        for a,b,c in costs:
            if a in bridge and b in bridge:
                continue
            if a in bridge or b in bridge:
                bridge.add(a)
                bridge.add(b)
                answer+=c
                break
    
    return answer