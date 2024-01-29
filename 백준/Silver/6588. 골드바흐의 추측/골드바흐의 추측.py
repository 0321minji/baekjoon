import sys, math
input=sys.stdin.readline

def prime():
    for i in range(2,int(math.sqrt(10**6))+1):
        if number[i]:
            for j in range(2*i,10**6+1,i):
                number[j]=0


number=[1]*(10**6+1)
prime()

while True:
    n=int(input())
    if not n:
        break
    
    for i in range(n-3,2,-2):
        if number[i] and number[n-i]:
            print(f"{n} = {n-i} + {i}") 
            break
        
    else:
        print("Goldbach's conjecture is wrong.")
 
