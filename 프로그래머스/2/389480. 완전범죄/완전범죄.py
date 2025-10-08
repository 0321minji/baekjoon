def solution(info, n, m):
    answer = 0
    INF=10**9
    dp=[INF]*(m)
    #최소 A의 흔적 합= b가 남긴 흔적일 때 dp[b]
    dp[0]=0
    #dp
    
    for a,b in info:
        dp2=[INF]*m
        for cur_b in range(m):
            if dp[cur_b]==INF:
                continue
            cur_a=dp[cur_b]
            
            #a가 훔치는 경우
            new_a=cur_a+a
            if new_a<n:
                dp2[cur_b]=min(new_a,dp2[cur_b])
            
            #b가 훔치는 경우
            new_b=cur_b+b
            if new_b<m:
                dp2[new_b]=min(cur_a,dp2[new_b])
            
            new_a=cur_a
        dp=dp2
    ans=min(dp)
    print(dp)
    return ans if ans!=INF else -1