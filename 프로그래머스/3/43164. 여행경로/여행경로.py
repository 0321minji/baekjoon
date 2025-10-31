from collections import defaultdict

def solution(tickets):
    answer = []
    t=defaultdict(list)
    n=len(tickets)+1
    
    for a,b in tickets:
        t[a].append(b)
        
    
    def dfs(level,routes,now):
        # print(routes)
        if level==n:
            answer.append(routes)
            return
        
        for nxt in t[now][:]:
            t[now].remove(nxt)
            dfs(level+1,routes+[nxt],nxt)
            t[now].append(nxt)
        return
        
    dfs(1,['ICN'],'ICN')
    answer.sort()
    # print(answer)
    return answer[0]
    # return 0