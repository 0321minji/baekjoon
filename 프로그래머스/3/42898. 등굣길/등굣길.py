def check(i,j,m,n,load):

    for i in range(2,m+1):
        for j in range(2,n+1):
            if load[j][i]:
                load[j][i]=load[j-1][i]+load[j][i-1]
    return load
    
def solution(m, n, puddles):
    answer = 0
    load=[[1]*(m+1) for _ in range(n+1)]
    for x,y in puddles:
        if x == 1:
            for i in range(y, n+1):
                load[i][x] = 0
        if y == 1:
            for i in range(x, m+1):
                load[y][i] = 0
    for x, y in puddles:
        load[y][x] = 0
        
    answer=check(1,1,m,n,load)[n][m]
    answer%=1000000007
    return answer