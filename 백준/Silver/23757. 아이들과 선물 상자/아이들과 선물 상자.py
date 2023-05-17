import heapq as hq
# python에서는 기본적으로 최소 힙이므로 문제 해결을 위해 최대힙으로 변경
n, m = map(int, input().split())
present = []
for x in list(map(int, input().split())):
    hq.heappush(present, -x) # 최대 힙 구현을 위하여 인자 -로 삽입
wish = list(map(int, input().split()))

ispre = False # 선물이 남는지 안남는지 확인 False 일 시 선물이 아이들 모두 분배
for i in wish:
    x = -hq.heappop(present)
    if x - i < 0:
        ispre = True # True 면 선물이 부족하다는 뜻
        break
    hq.heappush(present, -(x-i))

if ispre:
    print(0)
else:
    print(1)