import sys
from itertools import permutations
input=sys.stdin.readline

n,m=map(int,input().split())

# 4가지 이동 (-2,1) / (-1,2) / (1,2) / (2,1)
# 어쩃든 오른쪽으로는 이동 & 한 사이클 이동 후에는 오른쪽으로 +6
# 상하로는 이동 자유로움
# n==1이면 이동 불가
if n==1:
    print(1)
# n==2 면, -1/+1 로만 상하이동 가능 -> ceil((m)/2) 번 이동 가능
elif n==2:
    print(min(4,(m+1)//2))
# n==3 이상이고 m이 6 이하면, 한 사이클(4칸) 또는 m번 이동 가능
elif n>=3 and m<=6:
    print(min(4,m))
# 그 외 , 한 사이클당 4칸 방문 가능 & 6칸 증가
else:
    print(m-2)
