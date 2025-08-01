n,k=map(int,input().split())

belts=list(map(int,input().split()))
cnt=0
index=0
robots=[False]*n
depth=0
while cnt<=k:
    depth+=1
    ## 벨트 회전
    # 벨트 시작 인덱스
    index=index-1 if index-1>=0 else 2*n-1
    # 로봇 회전
    for i in range(n-2,-1,-1):
        robots[i+1]=robots[i]
    robots[0]=False
    if robots[-1]==True:
        robots[-1]=False
    
    ## 로봇 이동
    for i in range(n-2,-1,-1):
        # 다음 칸 이동
        if robots[i]:
            tmp=(index+i+1)%(2*n)
            if not robots[i+1] and belts[tmp]>0:
                belts[tmp]-=1
                if belts[tmp]==0:
                    cnt+=1
                robots[i+1]=True
                robots[i]=False
        # 내리는 칸
        if i+1==n-1:
            robots[i+1]=False
            
    ## 로봇 올리기
    if belts[index]>0:
        belts[index]-=1
        if belts[index]==0:
            cnt+=1
        robots[0]=True

    if cnt>=k:
        print(depth)
        break
