import sys
input = sys.stdin.readline
n, k = map(int, input().split())
score = []
for i in range(n):
    score.append(list(map(int, input().split())))
score.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if score[i][0] == k:
        index = i
        break
for i in range(n):
    if score[index][1:] == score[i][1:]:
        print(i + 1)
        break  
