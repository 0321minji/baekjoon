n=int(input())
answer=float("inf")

temp=n//5

for i in range(temp+1):
    five=i
    three=(n-i*5)//3
    if (n-i*5)%3:
        continue
    answer=min(three+five,answer)

print(answer if answer!=float("inf") else -1)
