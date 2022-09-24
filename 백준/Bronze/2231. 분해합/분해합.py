n=int(input())

for i in range(1,n):
    Sum=i
    temp=i
    while temp:
        Sum+=temp%10
        temp//=10
    if n==Sum:
        print(i)
        exit()
print(0)