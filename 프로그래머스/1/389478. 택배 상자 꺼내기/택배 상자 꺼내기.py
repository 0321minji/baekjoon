def solution(n, w, num):
    answer = 0
    h = n//w+1
    graph=[[0 for _ in range(w)] for _ in range(h)]
    x=0
    y=h-1
    
    gx=gy=0
    
    # 택배 쌓기
    for i in range(1,n+1):
        graph[y][x]=i
        if i == num:
            gx=x; gy=y

        # w로 나누었을때 짝수면 오른쪽 홀수면 왼쪽
        now = i//w
        # print('now',now,'i',i,i%w)
        if i%w==0:
            y-=1
            continue
        if now%2:
            x-=1
        else:
            x+=1
            
#     print(graph)
#     print(gy,gx)
    #개수 구하기
    for i in range(y,gy+1):
        print(i,gx,graph[i][gx])
        if graph[i][gx]:

            answer+=1
    
    return answer