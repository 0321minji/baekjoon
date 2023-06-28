t=int(input())

def fact(n):
    if n==1:
        return n
    else:
        return(n*fact(n-1))
        
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print(1)
        continue
    temp=fact(b)//fact(a)//fact(b-a)
    print(temp)
