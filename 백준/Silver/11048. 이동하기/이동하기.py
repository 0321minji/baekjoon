import sys
input=sys.stdin.readline

def solve():
    
    for i in range(n):
        for j in range(m):
            if i==0 and j==0: continue
            if i>=1 and j>=1:
                candy[i][j]=max(candy[i-1][j],candy[i][j-1],candy[i-1][j-1])+candy[i][j]
            elif i==0:
                candy[i][j]=candy[i][j-1]+candy[i][j]
            elif j==0:
                candy[i][j]=candy[i-1][j]+candy[i][j]


    
n,m=map(int,input().split())
candy=[list(map(int,input().split())) for _ in range(n)]
solve()
print(candy[n-1][m-1])
    
