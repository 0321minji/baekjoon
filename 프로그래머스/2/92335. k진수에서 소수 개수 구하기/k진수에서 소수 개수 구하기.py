def solution(n, k):
    answer = 0
    nums="0123456789"
    
    # n -> k 진수 변환
    def change(num,k):
        rev=''
        while num>0:
            num,mod=divmod(num,k)
            rev+=nums[mod]
        # print(rev)
        return rev[::-1]
    
    # 소수판별법 호제
    def is_prime(num):
        if num==1:
            return False
        if num==2:
            return True
        end=int(num**(1/2))
        for i in range(2,end+1):
            if num%i==0:
                return False
        return True
    
    # 걍 0을 기준으로 끊어서 그 숫자들이 소수인지 아닌지 판단
    num=change(n,k)
    temp=''
    for i in num:
        if i>'0':
            temp+=i
        else:
            if temp and is_prime(int(temp)):
                answer+=1
            temp=''
    if temp and is_prime(int(temp)):
        answer+=1
    
    return answer