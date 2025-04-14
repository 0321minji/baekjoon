import sys 
input= sys.stdin.readline

n=int(input())
x=list(map(int,input().split()))

# 중복 제거
number = list(set(x))
number.sort()

# 시간 초과 O(N^2)
# for t in x:
#     print(number.index(t),end=" ")

# 개선
dic = {number[i] : i for i in range(len(number))}

for t in x :
    print(dic[t],end=' ')