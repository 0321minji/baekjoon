import sys


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n, m = map(int, input().split())  # n : 점의 개수, m : 진행된 차례의 수
parent = list(range(n))

for i in range(m):
    x, y = map(int, input().split())
    if find_parent(parent, x) == find_parent(parent, y):  # 사이클 발생시
        print(i + 1)
        exit(0)
    union(parent, x, y)  # 점 잇기
else:  # m번의 차례를 모두 처리한 이후에도 종료되지 않았다면
    print(0)