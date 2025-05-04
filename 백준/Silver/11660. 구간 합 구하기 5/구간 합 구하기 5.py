import sys
input=sys.stdin.readline

n,m=map(int,input().split())
num=[[0 for _ in range(n)] for _ in range(n)]
pre=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range (n):
    num[i]=list(map(int,input().split()))
for i in range (1,n+1):
    for j in range(1,n+1):
        pre[i][j]=-pre[i-1][j-1]+pre[i][j-1]+pre[i-1][j]+num[i-1][j-1] #num은 0,0시작임
for k in range (m):
    a,b,c,d=map(int,input().split())
    ans=pre[c][d]-pre[a-1][d]-pre[c][b-1]+pre[a-1][b-1]#0,0시작이므로
    print(ans)
    