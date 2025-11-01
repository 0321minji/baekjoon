def solution(arr):
    answer = 0

    ##에라토스테네스의 체
    def gcd(m,n):
        while n!=0:
            t=m%n
            m,n=n,t
        return abs(m)
    def lcm(m,n):
        return m//gcd(m,n)*n
    
    answer=arr[0]
    for i in range(1,len(arr)):
        answer=lcm(answer,arr[i])
    
    return answer