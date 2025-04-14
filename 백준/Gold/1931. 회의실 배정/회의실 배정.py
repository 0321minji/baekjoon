import sys 
input= sys.stdin.readline

n=int(input())
time = [list(map(int,input().split())) for _ in range(n)]
time.sort(key=lambda x:(x[1],x[0]))

now = time[0][1]
result=1
for start, end in time[1:]:
    if now<=start:
        now = end
        result+=1
print(result)