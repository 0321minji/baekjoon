#1758
import sys
input=sys.stdin.readline

n=int(input())
tip=[]
for i in range(n):
    tip.append(int(input()))

total=0
tip.sort(reverse=True)
for i in range(n):
    temp=tip[i]-i
    if temp>=0:
        total+=temp

print(total)
