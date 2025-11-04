from itertools import permutations
def solution(numbers):
    answer = 0
    prime=set()
    
    def isPrime(num):
        if num<=1:
            return False
        for i in range(2,int(num**1/2)+1):
            if num%i==0:
                return False
        return True

    nums=list(numbers)
    # print(nums)
    n=len(nums)
    for i in range(1,n+1):
        for pr in permutations(nums,i):
            temp=int("".join(pr))
            if isPrime(temp):
                if temp not in prime:
                    answer+=1
                    prime|=set([temp])
                    print(temp,prime,answer)

    return answer