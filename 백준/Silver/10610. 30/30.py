n=list(input())
n.sort(reverse=True)

result=int("".join(n))

if result%30==0:
    print(result)
else:
    print(-1)
