n=int(input())
v = list(map(int, input().split()))
maxheight=0
ans=0
a=0

for i in range(n):
    if(maxheight<v[i]):
        maxheight=v[i]
        ans=max(ans,a)
        a = -1
    a+=1
    
ans=max(ans,a)
print(ans)