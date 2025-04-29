import sys
input=sys.stdin.readline
from collections import defaultdict
## 시작하기전에 한 번 / 끝난 이후~ 스트리밍 끝난 이전에 한 번
## 조건 비교해서 입장 / 퇴장 체크 입장에 있으면 -> cnt +=1

s,e,q= map(str,input().split())
attend = defaultdict(int)
st,sm=map(int,s.split(":"))
et,em=map(int,e.split(":"))
qt,qm=map(int,q.split(":"))

ss=st*60+sm
ee=et*60+em
qq=qt*60+qm
cnt=0

while(True):
    try:
        time, name = map(str,input().split())
        t,m = map(int,time.split(":"))
        tt=t*60+m
        # 참석
        if tt<=ss:
            attend[name]=1
        # 퇴장
        elif ee<=tt<=qq:
            if attend[name]==1:
                cnt+=1
                attend[name]+=1
    except:
        print(cnt)
        break