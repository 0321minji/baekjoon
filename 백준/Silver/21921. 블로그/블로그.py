import sys
input=sys.stdin.readline

def check():
    temp=sum(visit[:x])
    cnt=1
    MAX=temp
    
    for i in range(x,n):
        temp += visit[i] - visit[i-x]
        # print(temp,MAX,cnt)
        if temp>MAX:
            MAX=temp
            cnt=1
        elif temp==MAX:
            cnt+=1
    
    if MAX:
        print(MAX)
        print(cnt)
    else:
        print("SAD")
    

n,x=map(int,input().split())
visit=list(map(int,input().split()))

check()