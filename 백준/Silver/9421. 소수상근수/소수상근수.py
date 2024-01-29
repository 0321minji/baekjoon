import sys, math
input=sys.stdin.readline

def prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True

def check(num):
    c={}

    while True:
        m=str(num)
        temp=0
        for i in range(len(m)):
            temp+=int(m[i])**2

        if temp==1:
            return True
        if temp in c:
            #print(temp,c)
            return False
        else:
            c[temp]=1
        num=temp

n=int(input())
for i in range(7,n+1):
    if prime(i) and check(i):
        print(i)
